import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# ------------------------------
# Page Title
# ------------------------------
st.title("📈 Choose the Stock")

# ------------------------------
# Stock List (US stocks - 8)
# ------------------------------
stocks = {
    "Apple (AAPL)": "AAPL",
    "Microsoft (MSFT)": "MSFT",
    "Amazon (AMZN)": "AMZN",
    "Google (GOOGL)": "GOOGL",
    "Tesla (TSLA)": "TSLA",
    "Meta (META)": "META",
    "NVIDIA (NVDA)": "NVDA",
    "Netflix (NFLX)": "NFLX"
}

# ------------------------------
# User Inputs
# ------------------------------
selected_stock = st.selectbox("Select a Stock", list(stocks.keys()))
years = st.number_input("Number of Years", min_value=1, max_value=10, value=5)

# ------------------------------
# Date Range
# ------------------------------
end_date = datetime.today()
start_date = end_date - timedelta(days=years * 365)

# ------------------------------
# Fetch Data
# ------------------------------
stock_ticker = stocks[selected_stock]
market_ticker = "^GSPC"  # S&P 500

# stock_data = yf.download(stock_ticker, start=start_date, end=end_date)["Close"]
# market_data = yf.download(market_ticker, start=start_date, end=end_date)["Close"]

stock_df = yf.download(
    stock_ticker,
    start=start_date,
    end=end_date,
    auto_adjust=True,
    progress=False
)

market_df = yf.download(
    market_ticker,
    start=start_date,
    end=end_date,
    auto_adjust=True,
    progress=False
)

# Safety check
if stock_df.empty or market_df.empty:
    st.error("⚠️ Data not available. Please try another stock or time period.")
    st.stop()

stock_data = stock_df["Close"]
market_data = market_df["Close"]



# ------------------------------
# Returns Calculation
# ------------------------------
stock_returns = stock_data.pct_change().dropna()
market_returns = market_data.pct_change().dropna()

returns_df = pd.concat([stock_returns, market_returns], axis=1)
returns_df.columns = ["Stock Returns", "Market Returns"]

# ------------------------------
# Beta Calculation
# ------------------------------
covariance = np.cov(returns_df["Stock Returns"], returns_df["Market Returns"])[0][1]
market_variance = np.var(returns_df["Market Returns"])
beta = covariance / market_variance

# ------------------------------
# Return Calculation
# ------------------------------
total_stock_return = float((stock_data.iloc[-1] / stock_data.iloc[0] - 1) * 100)
total_market_return = float((market_data.iloc[-1] / market_data.iloc[0] - 1) * 100)

# total_stock_return = (stock_data.iloc[-1] / stock_data.iloc[0] - 1) * 100
# total_market_return = (market_data.iloc[-1] / market_data.iloc[0] - 1) * 100

# ------------------------------
# Display Metrics
# ------------------------------
st.subheader("📊 Performance Summary")

col1, col2, col3 = st.columns(3)
col1.metric("Stock Return (%)", f"{total_stock_return:.2f}")
col2.metric("Market Return (%)", f"{total_market_return:.2f}")
col3.metric("Beta", f"{beta:.2f}")

# ------------------------------
# Scatter Plot + Trend Line
# ------------------------------
st.subheader("📉 Stock vs Market Returns")

reg_df = returns_df.replace([np.inf, -np.inf], np.nan).dropna()

if len(reg_df) < 10:
    st.warning("⚠️ Not enough data points for regression.")
    st.stop()

x = reg_df["Market Returns"].values
y = reg_df["Stock Returns"].values

try:
    m, c = np.polyfit(x, y, 1)
    trend_line = m * x + c
except np.linalg.LinAlgError:
    st.error("⚠️ Regression failed. Try another stock or time range.")
    st.stop()

fig, ax = plt.subplots()
ax.scatter(x, y, alpha=0.5, label="Daily Returns")
ax.plot(x, trend_line, color="red", label="Expected Return Line")
ax.set_xlabel("Market Returns")
ax.set_ylabel("Stock Returns")
ax.legend()
ax.grid(True)

st.pyplot(fig)

