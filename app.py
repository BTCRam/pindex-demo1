import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="RingZk Performance Evaluation", layout="centered")
st.title("Performance Evaluation of RingZk vs zk-SNARK vs zk-STARK")

# ---------------------------------------------------
# Common Transaction Scale
# ---------------------------------------------------
transactions = [1, 3, 6, 10, 20, 30, 40, 50]

# ---------------------------------------------------
# Helper Function – Segregated Bar Chart (FINAL FIX)
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
            header=alt.Header(labelOrient="bottom")
        )
    ).properties(
        width=120,   # IMPORTANT: facet width
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

st.altair_chart(
    segregated_bar_chart(
        tat_data,
        "Turnaround Time (ms)",
        "Transaction Turnaround Time Comparison",
        "Time (ms)"
    )
)

# ---------------------------------------------------
# 2. Memory Consumption (MB)
# ---------------------------------------------------
memory_data = pd.DataFrame({
    "Transactions": transactions,
    "RingZk": [11, 13, 17, 20, 22, 20, 26, 23],
    "zk-SNARK": [8, 17, 21, 22, 23, 21, 29, 32],
    "zk-STARK": [10, 19, 21, 23, 24, 21, 30, 31]
})

st.altair_chart(
    segregated_bar_chart(
        memory_data,
        "Memory (MB)",
        "Memory Consumption Comparison",
        "Memory (MB)"
    )
)

# ---------------------------------------------------
# 3. Throughput (tx/sec)
# ---------------------------------------------------
throughput_data = pd.DataFrame({
    "Transactions": transactions,
    "RingZk": [500, 490, 475, 480, 500, 465, 500, 500],
    "zk-SNARK": [450, 400, 300, 200, 250, 180, 260, 280],
    "zk-STARK": [440, 360, 320, 200, 240, 170, 150, 70]
})

st.altair_chart(
    segregated_bar_chart(
        throughput_data,
        "Throughput (tx/sec)",
        "Throughput Comparison",
        "Transactions per Second"
    )
)

# ---------------------------------------------------
# 4. Time Taken for Anonymity Transaction (ms)
# ---------------------------------------------------
anon_time_data = pd.DataFrame({
    "Transactions": transactions,
    "RingZk": [30, 45, 60, 120, 100, 100, 120, 140],
    "zk-SNARK": [50, 100, 150, 1000, 2500, 2000, 2800, 3300],
    "zk-STARK": [60, 120, 550, 1700, 2000, 1700, 2800, 3700]
})

st.altair_chart(
    segregated_bar_chart(
        anon_time_data,
        "Anonymity Time (ms)",
        "Time Taken for Anonymity Transaction",
        "Time (ms)"
    )
)

# ---------------------------------------------------
# Interpretation
# ---------------------------------------------------
st.success(
    "Summary:\n"
    "• RingZk demonstrates stable performance across all transaction scales.\n"
    "• zk-SNARK and zk-STARK incur higher computation and anonymity overhead.\n"
    "• Throughput degradation is evident in zk-based schemes.\n"
    "• RingZk achieves efficient privacy preservation with lower cost."
)

st.caption(
    "Note: Experimental values are aligned with the comparative performance "
    "evaluation of RingZk, zk-SNARK, and zk-STARK."
)

