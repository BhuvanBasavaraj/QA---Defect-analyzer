import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="DEFECT",
    page_icon="●",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "dashboard"

if "report" not in st.session_state:
    st.session_state.report = None

if "raw_defect" not in st.session_state:
    st.session_state.raw_defect = ""


# =========================================================
# CUSTOM STYLING
# No visible HTML is used.
# =========================================================

st.markdown(
    """
    <style>

    /* ==============================
       GLOBAL
       ============================== */

    .stApp {
        background-color: #070a08;
        color: #e8eee9;
    }

    .block-container {
        max-width: 1350px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* ==============================
       SIDEBAR
       ============================== */

    section[data-testid="stSidebar"] {
        background-color: #090d0b;
        border-right: 1px solid #1b251f;
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 2rem;
    }

    section[data-testid="stSidebar"] .stButton button {
        background: transparent;
        border: 1px solid transparent;
        color: #7d8981;
        text-align: left;
        justify-content: flex-start;
    }

    section[data-testid="stSidebar"] .stButton button:hover {
        background: #111812;
        border-color: #26372c;
        color: #ffffff;
    }


    /* ==============================
       BUTTONS
       ============================== */

    .stButton > button {
        min-height: 44px;
        border-radius: 8px;
        border: 1px solid #26362c;
        background: #0d130f;
        color: #d7dfda;
        font-weight: 600;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        border-color: #4ade80;
        background: #101a13;
        color: #ffffff;
    }


    /* ==============================
       PRIMARY BUTTON
       ============================== */

    div.stButton > button[kind="primary"] {
        background: #39a862;
        border-color: #39a862;
        color: #061009;
    }

    div.stButton > button[kind="primary"]:hover {
        background: #4ade80;
        border-color: #4ade80;
        color: #061009;
    }


    /* ==============================
       TEXT AREA
       ============================== */

    textarea {
        background-color: #0b100d !important;
        color: #e8eee9 !important;
        border: 1px solid #26362c !important;
        border-radius: 10px !important;
        font-size: 14px !important;
        line-height: 1.7 !important;
    }

    textarea:focus {
        border-color: #42b96c !important;
        box-shadow: 0 0 0 1px #42b96c !important;
    }


    /* ==============================
       METRICS
       ============================== */

    [data-testid="stMetric"] {
        background: #0c120e;
        border: 1px solid #1d2a21;
        border-radius: 12px;
        padding: 18px;
    }

    [data-testid="stMetricLabel"] {
        color: #68756d !important;
    }

    [data-testid="stMetricValue"] {
        color: #eef4f0 !important;
    }


    /* ==============================
       DIVIDERS
       ============================== */

    hr {
        border-color: #1b251f;
    }


    /* ==============================
       ALERTS
       ============================== */

    [data-testid="stAlert"] {
        background: #0d1510;
        border: 1px solid #26372c;
    }


    /* ==============================
       DOWNLOAD
       ============================== */

    .stDownloadButton button {
        background: #0d130f;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## :green[DEFECT]")
    st.caption("QA ISSUE MANAGEMENT")

    st.divider()

    st.caption("WORKSPACE")

    if st.button("Dashboard", use_container_width=True):
        st.session_state.page = "dashboard"
        st.rerun()

    if st.button("New Defect", use_container_width=True):
        st.session_state.page = "new_defect"
        st.rerun()

    if st.button("Reports", use_container_width=True):
        st.session_state.page = "reports"
        st.rerun()

    if st.button("History", use_container_width=True):
        st.session_state.page = "history"
        st.rerun()

    st.divider()

    st.caption("SYSTEM")

    if st.button("Settings", use_container_width=True):
        st.session_state.page = "settings"
        st.rerun()

    st.write("")
    st.write("")

    st.caption("DEFECT/01")
    st.caption("QA workspace")
    st.caption("Version 1.0")


# =========================================================
# DASHBOARD
# =========================================================

if st.session_state.page == "dashboard":

    st.caption("QA / DASHBOARD")

    st.title("Keep every defect clear.")

    st.write(
        "Capture issues quickly, structure defect reports, "
        "and keep your testing workflow organized."
    )

    st.write("")

    # Main action
    left, center, right = st.columns([1, 1.2, 1])

    with center:
        if st.button(
            "＋  Raise New Defect",
            type="primary",
            use_container_width=True,
        ):
            st.session_state.page = "new_defect"
            st.rerun()

    st.write("")
    st.divider()

    # Overview
    st.subheader("Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Total Defects",
            value="128",
            delta="12 this week",
        )

    with col2:
        st.metric(
            label="Open",
            value="34",
            delta="8 need attention",
            delta_color="inverse",
        )

    with col3:
        st.metric(
            label="Resolved",
            value="81",
            delta="63%",
        )

    with col4:
        st.metric(
            label="Reports",
            value="96",
            delta="This month",
        )

    st.write("")
    st.subheader("Recent Defects")

    # Recent defects
    defects = [
        (
            "DF-0128",
            "Login fails after valid credentials",
            "High",
            "Open",
        ),
        (
            "DF-0127",
            "Dashboard data not refreshed",
            "Medium",
            "Review",
        ),
        (
            "DF-0126",
            "Export report returns empty file",
            "High",
            "Fixed",
        ),
        (
            "DF-0125",
            "Profile image upload timeout",
            "Low",
            "Open",
        ),
    ]

    for defect_id, title, severity, status in defects:

        with st.container(border=True):

            c1, c2, c3 = st.columns([1.2, 5, 1.3])

            with c1:
                st.caption(defect_id)
                st.write(severity)

            with c2:
                st.write(f"**{title}**")
                st.caption("Recently reported")

            with c3:
                st.write(status)


# =========================================================
# NEW DEFECT
# =========================================================

elif st.session_state.page == "new_defect":

    st.caption("QA / NEW DEFECT")

    if st.button("← Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.session_state.report = None
        st.rerun()

    st.title("New Defect")

    st.write(
        "Describe the issue in your own words. "
        "The report can be structured after you submit it."
    )

    st.write("")

    defect_text = st.text_area(
        "Defect description",
        value=st.session_state.raw_defect,
        height=220,
        placeholder=(
            "Example:\n\n"
            "The login button does not work after entering "
            "valid credentials."
        ),
        label_visibility="visible",
    )

    st.session_state.raw_defect = defect_text

    st.write("")

    if st.button(
        "Enhance Report",
        type="primary",
        use_container_width=True,
    ):

        if not defect_text.strip():

            st.warning("Please enter a defect description.")

        else:

            # -------------------------------------------------
            # DEMO RESPONSE
            # Replace this block with your AI/backend later.
            # -------------------------------------------------

            st.session_state.report = {
                "title": "Login fails after valid credentials",

                "description": (
                    "The application does not complete the login "
                    "request after valid credentials are entered."
                ),

                "steps": [
                    "Open the application.",
                    "Navigate to the Login page.",
                    "Enter a valid username.",
                    "Enter a valid password.",
                    "Click the Login button.",
                ],

                "expected": (
                    "The user should be authenticated and "
                    "redirected to the application dashboard."
                ),

                "actual": (
                    "The user remains on the Login page and "
                    "the login request does not complete."
                ),

                "severity": "High",
                "priority": "High",
            }

            st.rerun()


    # =====================================================
    # REPORT
    # =====================================================

    if st.session_state.report:

        report = st.session_state.report

        st.write("")
        st.divider()

        st.subheader("Enhanced Report")
        st.caption("READY FOR REVIEW")

        with st.container(border=True):

            st.write("**Title**")
            st.write(report["title"])

            st.divider()

            st.write("**Description**")
            st.write(report["description"])

            st.divider()

            st.write("**Steps to Reproduce**")

            for index, step in enumerate(
                report["steps"],
                start=1,
            ):
                st.write(f"{index}. {step}")

            st.divider()

            expected_col, actual_col = st.columns(2)

            with expected_col:

                st.write("**Expected Result**")
                st.write(report["expected"])

            with actual_col:

                st.write("**Actual Result**")
                st.write(report["actual"])

            st.divider()

            severity_col, priority_col = st.columns(2)

            with severity_col:

                st.write("**Severity**")
                st.success(report["severity"])

            with priority_col:

                st.write("**Priority**")
                st.success(report["priority"])

        st.write("")

        # Plain text report
        report_text = f"""
DEFECT REPORT

Title
{report["title"]}

Description
{report["description"]}

Steps to Reproduce

{chr(10).join(
    f"{i}. {step}"
    for i, step in enumerate(report["steps"], 1)
)}

Expected Result
{report["expected"]}

Actual Result
{report["actual"]}

Severity
{report["severity"]}

Priority
{report["priority"]}
""".strip()

        col1, col2 = st.columns(2)

        with col1:

            st.download_button(
                "Download Report",
                data=report_text,
                file_name="defect-report.txt",
                mime="text/plain",
                use_container_width=True,
            )

        with col2:

            if st.button(
                "＋ Create Another Defect",
                use_container_width=True,
            ):

                st.session_state.report = None
                st.session_state.raw_defect = ""
                st.rerun()


# =========================================================
# REPORTS
# =========================================================

elif st.session_state.page == "reports":

    st.caption("QA / REPORTS")

    st.title("Reports")

    st.write("Your generated defect reports will appear here.")

    st.write("")

    with st.container(border=True):

        st.subheader("No saved reports")

        st.write(
            "Create a new defect to generate your first "
            "structured QA report."
        )

        if st.button(
            "Create New Defect",
            type="primary",
        ):
            st.session_state.page = "new_defect"
            st.rerun()


# =========================================================
# HISTORY
# =========================================================

elif st.session_state.page == "history":

    st.caption("QA / HISTORY")

    st.title("History")

    st.write("Previously created defects will appear here.")

    st.write("")

    with st.container(border=True):

        st.subheader("No defect history")

        st.write(
            "Once defects are created, their history can "
            "be displayed here."
        )


# =========================================================
# SETTINGS
# =========================================================

elif st.session_state.page == "settings":

    st.caption("QA / SETTINGS")

    st.title("Settings")

    st.write("Application configuration.")

    st.write("")

    with st.container(border=True):

        st.subheader("Workspace")

        st.checkbox(
            "Keep generated reports locally",
            value=True,
        )

        st.checkbox(
            "Show defect confirmation",
            value=True,
        )

        st.divider()

        st.write("**Application version**")
        st.write("DEFECT/01 · v1.0")


# =========================================================
# FOOTER
# =========================================================

st.write("")
st.write("")
st.divider()
st.caption("DEFECT/01 · QA ISSUE MANAGEMENT · v1.0")
