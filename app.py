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

systems =
