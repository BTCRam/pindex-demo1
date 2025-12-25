import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------------
# Title and Caption
# --------------------------------------------------
st.title("Comparative Performance Analysis of Zero-Knowledge Frameworks")
st.caption("Controlled smart contract experiments on Ethereum-compatible private blockchain")

# --------------------------------------------------
# Experimental Context
# --------------------------------------------------
st.info("""
### Experimental Setup
- Ethereum-compatible private blockchain test network  
- Smart contracts written in Solidity  
- Batch execution of privacy-preserving transactions  
- Zero-knowledge verification executed on-chain  
- Metrics captured at smart contract execution layer  
""")

st.info("""
### Evaluation Scope
- Comparison between RingZk, zk-SNARK, and zk-STARK  
- Metrics: Execution Time, Memory Usage, Throughput, Scalability  
- Transactions executed under identical test conditions  
""")

# --------------------------------------------------
# Sample Data
# --------------------------------------------------
transactions = [1, 3, 6, 10, 20, 30, 40, 50]

data = {
    "RingZk": {
        "Time": [5, 10, 20, 300, 270, 60, 70, 50],
        "Memory": [18, 20, 21, 22, 23, 22, 28, 24],
        "Throughput": [500, 500, 500, 200, 250, 180, 150, 70],
        "AnonymityTime": [10, 30, 100, 500, 2500, 2000, 2700, 3200]
    },
    "zkSNARK": {
        "Time": [8, 15, 25, 310, 280, 65, 75, 55],
        "Memory": [17, 21, 22, 23, 24, 21, 29, 31],
        "Throughput": [450, 400, 300, 200, 240, 180, 250, 70],
        "AnonymityTime": [15, 35, 110, 1000, 2500, 2000, 2700, 3200]
    },
    "zkSTARK": {
        "Time": [10, 20, 30, 390, 280, 110, 60, 50],
        "Memory": [19, 20, 21, 23, 25, 22, 30, 31],
        "Throughput": [450, 350, 300, 200, 240, 180, 150, 70],
        "AnonymityTime": [20, 40, 120, 1700, 2000, 1600, 2700, 3600]
    }
}

# --------------------------------------------------
# Function to Plot Charts
# --------------------------------------------------
def plot_metric(metric_name, ylabel):
    plt.figure(figsize=(10,5))
    plt.plot(transactions, data['RingZk'][metric_name], marker='o', label='RingZk')
    plt.plot(transactions, data['zkSNARK'][metric_name], marker='o', label='zk-SNARK')
    plt.plot(transactions, data['zkSTARK'][metric_name], marker='o', label='zk-STARK')
    plt.xlabel("Number of Transactions")
    plt.ylabel(ylabel)
    plt.title(f"{metric_name} Comparison")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

# --------------------------------------------------
# Display Charts
# --------------------------------------------------
st.subheader("1. Transaction Turn Around Time Comparison")
plot_metric("Time", "Time (ms)")

st.subheader("2. Memory Consumption Comparison")
plot_metric("Memory", "Memory (MB)")

st.subheader("3. Throughput Comparison")
plot_metric("Throughput", "Throughput (B/s)")

st.subheader("4. Time Taken for Anonymity Transactions")
plot_metric("AnonymityTime", "Time (s)")
