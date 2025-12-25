import streamlit as st
import pandas as pd

# --------------------------------------------------
# Privacy Index Computation (as per paper definition)
# --------------------------------------------------
def compute_pindex(anonymity, unlinkability, confidentiality, resistance):
    weights = {
        "Anonymity": 0.30,
        "Unlinkability": 0.25,
        "Confidentiality": 0.25,
        "Resistance": 0.20
    }
    return round(
        anonymity * weights["Anonymity"] +
        unlinkability * weights["Unlinkability"] +
        confidentiality * weights["Confidentiality"] +
        resistance * weights["Resistance"],
        2
    )

# --------------------------------------------------
# Experimental Data (Aligned with Diagram Candidates)
# Qui, Han, He, Zhang, Proposed RingZk
# --------------------------------------------------
data = {
    "Method": [
        "Qui et al.",
        "Han et al.",
        "He et al.",
        "Zhang et al.",
        "Proposed RingZk"
    ],
    "Anonymity": [6.2, 6.8, 7.1, 7.5, 9.2],
    "Unlinkability": [5.9, 6.4, 6.9, 7.2, 9.0],
    "Confidentiality": [6.5, 7.0, 7.3, 7.8, 8.8],
    "Resistance": [6.0, 6.6, 6.8, 7.1, 8.7]
}

df = pd.DataFrame(data)

# --------------------------------------------------
# Compute Privacy Index
# --------------------------------------------------
df["Privacy Index"] = df.apply(
    lambda row: compute_pindex(
        row["Anonymity"],
        row["Unlinkability"],
        row["Confidentiality"],
        row["Resistance"]
    ),
    axis=1
)

# --------------------------------------------------
# Streamlit UI
# --------------------------------------------------
st.set_page_config(
    page_title="Privacy Index (PIndex) Demo",
    layout="centered"
)

st.title("Privacy Index (PIndex) – Comparative Evaluation")
st.caption("Live result visualization aligned with evaluation diagram")

# --------------------------------------------------
# Figure 1: Metric-wise Comparison (Table)
# --------------------------------------------------
st.subheader("Metric-wise Privacy Evaluation of Candidate Schemes")
st.table(
    df[[
        "Method",
        "Anonymity",
        "Unlinkability",
        "Confidentiality",
        "Resistance"
    ]]
)

# --------------------------------------------------
# Figure 2: Privacy Index Comparison (Bar Chart)
# --------------------------------------------------
st.subheader("Overall Privacy Index Comparison")
st.bar_chart(
    df.set_index("Method")["Privacy Index"]
)

# --------------------------------------------------
# Result Interpretation (Paper-consistent)
# --------------------------------------------------
st.success(
    "Result: Among all evaluated schemes (Qui, Han, He, Zhang, RingZk), "
    "the RingZk framework achieves the highest Privacy Index, "
    "demonstrating superior privacy preservation capability."
)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.caption("Note")
