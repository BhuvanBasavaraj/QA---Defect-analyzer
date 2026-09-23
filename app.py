from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import glob
import ollama
import re

app = FastAPI()

model = SentenceTransformer("all-MiniLM-L6-v2")


class DefectRequest(BaseModel):
    defect: str


def load_knowledge():
    files = glob.glob("knowledge/*.txt")
    chunks = []

    for file in files:
        text = open(file, encoding="utf-8").read()

        # Split complete examples
        parts = re.split(r"(?=EXAMPLE \d+)", text)

        for part in parts:
            if part.strip():
                chunks.append(part.strip())

    return chunks


@app.get("/")
def home():
    return {"message": "TCS Defect AI Backend is running"}


@app.post("/enhance")
def enhance_defect(request: DefectRequest):

    chunks = load_knowledge()

    document_embeddings = model.encode(chunks)

    query_embedding = model.encode([request.defect])

    scores = cosine_similarity(
        query_embedding,
        document_embeddings
    )[0]

    top_indices = scores.argsort()[-3:][::-1]

    retrieved_knowledge = ""

    for index in top_indices:
        retrieved_knowledge += chunks[index] + "\n\n"

    prompt = f"""
You are a software QA defect enhancement assistant.

Use the retrieved QA knowledge as reference.

--- RETRIEVED KNOWLEDGE ---
{retrieved_knowledge}
--- END KNOWLEDGE ---

--- RAW DEFECT ---
{request.defect}
--- END RAW DEFECT ---

Create a professional structured defect report.

Include exactly:

Title:
Description:
Steps to Reproduce:
Expected Result:
Actual Result:
Severity:
Priority:
Environment:
Missing Information:

IMPORTANT RULES:

1. Never invent facts.
2. Only use information explicitly present in the RAW DEFECT.
3. Retrieved examples are templates only.
4. Never copy device, OS, application version, severity, priority,
   dates, users, or other specific values from examples.
5. If severity cannot be determined:
Severity: Requires Review
6. If priority cannot be determined:
Priority: Requires Review
7. If environment is not provided:
Environment: Not Provided
8. Put unavailable information under Missing Information.
"""

    response = ollama.chat(
        model="qwen2.5:1.5b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "enhanced_defect": response["message"]["content"],
        "retrieved_knowledge": retrieved_knowledge
    }
