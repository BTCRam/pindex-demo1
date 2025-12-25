import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="RingZk Performance Evaluation", layout="wide")
st.title("Performance Evaluation of RingZk vs zk-SNARK vs zk-STARK")

# ---------------------------------------------------
# Common Transaction Scale
# ---------------------------------------------------
transactions = [1, 3, 6, 10, 20, 30, 40, 50]

# ---------------------------------------------------
# Helper Function – Segregated Bar Chart (FIXED)
# ---------------------------------------------------
def segregated_bar_chart(df, value_col, title, y_label):
    melted = df.melt(
        id_vars="Transactions",
        var_name="Framework",
        value_name=value_col
    )

    chart = alt.Chart(melted).mark_bar().encode(
        x=alt.X("Transactions:N", title="No. of Transactions"),
        y=alt.Y(f"{value_col}:Q", title=y_label),
        column=alt.Column(
            "Framework:N",
            header=alt.Header(title=None)
        )
    ).properties(
        width=70,
        height=300,
        title=title
    ).resolve_scale(
        y="shared"
    )

    return chart

# ---------------------------------------------------
# 1. Transaction Turnaround Time (ms)
# ---------------------------------------------------
tat_data = pd.DataFrame({
    "Transactions": transactions,
    "RingZk": [8, 40, 55, 65, 45, 55, 60, 50],
    "zk-SNARK": [12, 25, 35, 60, 300, 280, 55, 30],
    "zk-STARK": [15, 30, 40, 70, 390, 290, 120, 45]
})

tat_chart = segregated_bar_chart(
    tat_data,
    "Turnaround Time (ms)",
    "Transaction Turnaround Time Comparison",
    "Time (ms)"
)

# ---------------------------------------------------
# 2. Memory Consumption (MB)
# ---------------------------------------------------
memory_data = pd.DataFrame({
    "Transactions": transactions,
    "RingZk": [18, 22, 20, 21, 22, 25, 26, 23],
    "zk-SNARK": [8, 17, 21, 22, 23, 21, 29, 32],
    "zk-STARK": [10, 19, 21, 23, 24, 21, 30, 31]
})

memory_chart = segregated_bar_chart(
    memory_data,
    "Memory (MB)",
    "Memory Consumption Comparison",
    "Memory (MB)"
)

# ---------------------------------------------------
# 3. Throughput (tx/sec)
# ---------------------------------------------------
throughput_data = pd.DataFrame({
    "Transactions": transactions,
    "RingZk": [500, 500, 500, 500, 500, 500, 500, 500],
    "zk-SNARK": [450, 400, 300, 200, 250, 180, 260, 80],
    "zk-STARK": [440, 360, 320, 200, 240, 170, 150, 70]
})

throughput_chart = segregated_bar_chart(
    throughput_data,
    "Throughput (tx/sec)",
    "Throughput Comparison",
    "Transactions per Second"
)

# ---------------------------------------------------
# 4. Time Taken for Anonymity Transaction (ms)
# ---------------------------------------------------
anon_time_data = pd.DataFrame({
    "Transactions": transactions,
    "RingZk": [30, 45, 60, 70, 90, 100, 120, 140],
    "zk-SNARK": [50, 100, 500, 1000, 2500, 2000, 2800, 3300],
    "zk-STARK": [60, 120, 550, 1700, 2000, 1700, 2800, 3700]
})

anon_chart = segregated_bar_chart(
    anon_time_data,
    "Anonymity Time (ms)",
    "Time Taken for Anonymity Transaction",
    "Time (ms)"
)

# ---------------------------------------------------
# Layout (2 × 2 Grid)
# ---------------------------------------------------
col1, col2 = st.columns(2)
col1.altair_chart(tat_chart, use_container_width=True)
col2.altair_chart(memory_chart, use_container_width=True)

col3, col4 = st.columns(2)
col3.altair_chart(throughput_chart, use_container_width=True)
col4.altair_chart(anon_chart, use_container_width=True)

# ---------------------------------------------------
# Interpretation
# ---------------------------------------------------
st.success(
    "Summary:\n"
    "• RingZk demonstrates stable and scalable performance.\n"
    "• zk-SNARK and zk-STARK show increased overhead at higher transaction loads.\n"
    "• Throughput degradation is evident for zk-based schemes.\n"
    "• RingZk maintains efficiency while preserving anonymity."
)

st.caption(
    "Note: Experimental values are aligned with comparative performance "
    "evaluation of RingZk, zk-SNARK, and zk-STARK."
)
