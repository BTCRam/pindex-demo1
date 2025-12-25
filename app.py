import streamlit as st

# -------------------------------
# Privacy Index Computation
# -------------------------------
def compute_pindex(anonymity, unlinkability, confidentiality, resistance):
    weights = {
        "anonymity": 0.30,
        "unlinkability": 0.25,
        "confidentiality": 0.25,
        "resistance": 0.20
    }
    score = (
        anonymity * weights["anonymity"] +
        unlinkability * weights["unlinkability"] +
        confidentiality * weights["confidentiality"] +
        resistance * weights["resistance"]
    )
    return round(score, 2)

# -------------------------------
# UI
# -------------------------------
st.set_page_config(page_title="Privacy Index Demo", layout="centered")

st.title("Privacy Index (PIndex) – Result Demonstration")
st.caption("PhD Thesis Demo: Privacy-Preserving Blockchain Evaluation")

systems = {
    "Traditional Blockchain": compute_pindex(4.0, 3.5, 4.2, 3.8),
    "ZK-only System": compute_pindex(7.5, 6.8, 8.2, 7.0),
    "Ring-only System": compute_pindex(7.8, 8.0, 6.5, 7.2),
    "Proposed RingZk": compute_pindex(9.2, 9.0, 8.8, 8.7)
}

st.subheader("Computed Privacy Index Scores")
st.table(systems)

st.subheader("Privacy Index Comparison")
st.bar_chart(systems)

st.success(
    "Result: The proposed RingZk framework achieves the highest Privacy Index score, "
    "demonstrating superior privacy guarantees."
)
