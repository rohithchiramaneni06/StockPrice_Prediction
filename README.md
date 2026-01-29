📈 Stock Price Prediction & Portfolio Analysis – Streamlit App
📌 Overview

This project is a Streamlit-based Stock Market Analytics and Prediction Application designed to help users analyze stocks, evaluate portfolio risk and returns using CAPM, visualize technical indicators, and forecast future stock prices using ARIMA time-series modeling.

The application is modular, interactive, and suitable for data analyst / data science portfolios.

🧩 Project Modules

The application consists of 5 core modules, all orchestrated through a main Streamlit app.

1️⃣ App (app.py)

Acts as the main entry point of the application

Handles:

Navigation between different pages

Integration of all analytical modules

Streamlit layout and UI rendering

2️⃣ CAPM Beta Analysis (capm_beta.py)

Calculates Beta (β) for individual stocks

Compares:

Stock returns

Market returns

Key concepts implemented:

Risk measurement

Volatility comparison against the market

Visualizations:

Returns comparison plots

Beta interpretation

3️⃣ CAPM Returns & Portfolio Comparison (capm_returns.py)

Analyzes multiple companies within a portfolio

Compares:

Expected returns using CAPM

Actual historical returns

Beta values across stocks

Displays:

Portfolio-level insights

Risk vs return trade-off

Stock-wise performance comparison

4️⃣ Stock Analysis (stock_analysis.py)

Provides detailed analysis of a selected company

Includes:

Company fundamentals

Financial ratios

Technical analysis indicators

Charts & Indicators:

Candlestick chart

Line chart

RSI (Relative Strength Index)

MACD

Moving Averages (SMA)

Built using Plotly for interactive visualizations

5️⃣ Stock Price Prediction (stock_price_prediction.py)

Forecasts next 30 days of stock prices

Uses:

ARIMA (AutoRegressive Integrated Moving Average) model

Stationarity testing (ADF test)

Differencing logic

Outputs:

Predicted future prices

Forecast visualization

Model evaluation (RMSE)

📂 Folder Structure
├── app.py
├── capm_functions.py
├── pages/
│   ├── capm_beta.py
│   ├── capm_returns.py
│   ├── stock_analysis.py
│   ├── stock_price_prediction.py
│   └── utils/
│       ├── __init__.py
│       ├── plotly_figure.py
│       ├── model_train.py

🔧 Utilities (utils)

plotly_figure.py

Contains reusable Plotly chart functions

MACD, RSI, moving averages, candlestick charts

model_train.py

Time series preprocessing

ARIMA model training

Forecasting logic

Scaling and inverse scaling

🛠️ Tech Stack

Python

Streamlit – Web app framework

Pandas / NumPy – Data manipulation

Plotly – Interactive charts

Statsmodels – ARIMA modeling

Scikit-learn – Scaling & metrics

YFinance – Stock market data

📊 Key Features

✔ Interactive stock charts
✔ CAPM-based risk & return analysis
✔ Technical indicators (RSI, MACD, MA)
✔ Portfolio comparison
✔ Time-series forecasting (30-day horizon)
✔ Modular & scalable architecture
