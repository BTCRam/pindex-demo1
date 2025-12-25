import streamlit as st
import pandas as pd
import altair as alt

# Example: Memory Consumption Data
transactions = [1, 3, 6, 10, 20, 30, 40, 50]
memory_data = pd.DataFrame({
    "Transactions": transactions,
    "RingZk": [18, 22, 20, 21, 22, 25, 26, 23],
    "zk-SNARK": [8, 17, 21, 22, 23, 21, 29, 32],
    "zk-STARK": [10, 19, 21, 23, 24, 21, 30, 31]
})

# Melt the DataFrame for Altair
memory_melted = memory_data.melt(id_vars="Transactions", var_name="Framework", value_name="Memory (MB)")

# Altair grouped bar chart
chart = alt.Chart(memory_melted).mark_bar().encode(
    x=alt.X('Transactions:N', title='No. of Transactions'),
    y=alt.Y('Memory (MB):Q', title='Memory (MB)'),
    color='Framework:N',
    column='Framework:N'  # optional: separate columns per framework
).properties(
    width=60,
    height=300,
    title='Memory Consumption vs Number of Transactions'
)

st.altair_chart(chart)
