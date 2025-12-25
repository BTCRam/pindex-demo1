import streamlit as st
import pandas as pd

# --------------------------------------------------
# Privacy Index Computation
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
# Experimental Data
# --------------------------------------------------
methods = [
    "Qui et al.",
    "Han et al.",
    "He et al.",
    "Zhang et al.",
    "Proposed RingZk"
]

# Privacy metrics
privacy_data = {
    "Method": methods,
    "Anonymity": [6.2, 6.8, 7.1, 7.5, 9.2],
    "Unlinkability": [5.9, 6.4, 6.9, 7.2, 9.0],
    "Confidentiality": [6.5, 7.0, 7.3, 7.8, 8.8],
    "Resistance": [6.0, 6.6, 6.8, 7.1, 8.7]
}

df_privacy = pd.DataFrame(privacy_data)

df_privacy["Privacy Index"] = df_privacy.apply(
    lambda row: compute_pindex(
        row["Anonymity"],
        row["Unlinkability"],
        row["Confidentiality"],
        row["Resistance"]
    ),
    axis=1
)

# Gas fees
gas_data = {
    "Method": methods,
    "Average Gas Fees (ETH)": [0.05, 0.07, 0.06, 0.08, 0.04]
}
df_gas = pd.DataFrame(gas_data)

# Transaction throughput
throughput_data = {
    "Method": methods,
    "Transaction Throughput": [45, 40, 35, 38, 50]
}
df_throughput = pd.DataFrame(throughput_data)

# Execution time
time_data = {
    "Method": methods,
    "Execution Time (ms)": [3.5, 3.0, 2.8, 3.2, 2.0]
}
df_time = pd.DataFrame(time_data)

# --------------------------------------------------
# Streamlit UI
# --------------------------------------------------
st.set_page_config(
    page_title="Comparative Performance Analysis",
    layout="centered"
)

st.title("Comparative Analysis of Privacy-Preserving Blockchain Frameworks")
st.caption("Live experimental result visualization")

# Privacy Index
st.subheader("Privacy Index Comparison")
st.bar_chart(df_privacy.set_index("Method")["Privacy Index"])

# Gas Fees
st.subheader("Average Gas Fees (ETH)")
st.bar_chart(df_gas.set_index("Method")["Average Gas Fees (ETH)"])

# Transaction Throughput
st.subheader("Transaction Throughput Comparison")
st.bar_chart(df_throughput.set_index("Method")["Transaction Throughput"])

# Execution Time
st.subheader("Execution Time Analysis (ms)")
st.bar_chart(df_time.set_index("Method")["Execution Time (ms)"])

# Summary
st.success(
    "Result: The proposed RingZk framework achieves the highest Privacy Index, "
    "while reducing gas cost and execution time, and improving transaction throughput "
    "compared to existing schemes."
)

st.caption("Note: Experimental values correspond to the comparative analysis diagram in the paper.")

