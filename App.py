import streamlit as st
import yfinance as yf


st.set_page_config(
    page_title="CAPM",
    page_icon="chart_with_downwards_trend:",
    layout='wide'
)

st.title("Stock Price Prediction App:bar_chart:")

st.header("Welcome to Stock Price Prediction App using CAPM Model here we provide company full data analysis and prediction of stock price using Capital Asset Pricing Model")

st.markdown("Here We Provide Following Services:")

st.markdown("1. CAPM_Beta")
st.write("In this section, users can select a stock from a predefined list and specify the number of years for analysis. The app fetches historical stock prices and market index data, calculates total returns, and displays the results along with visualizations.")
st.markdown("2. CAPM_Return")
st.write("This section allows users to select multiple stocks and a " \
"time period for analysis. The app retrieves historical stock prices and " \
"market index data, merges them, and displays the combined DataFrame. It also " \
"provides visualizations of stock prices over time.")
st.markdown("3. Stock Analysis")
st.write("This section provides a comprehensive analysis of selected stocks. " \
"It fetches historical stock data, calculates key financial metrics, and " )
st.markdown("4. Stock Price Prediction")
st.write("In this section, users can select a stock and a time period for " \
"price prediction. The app retrieves historical stock prices, preprocesses the " \
"data, and uses a machine learning model to predict future stock prices. ")