import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import plotly.express as px
import datetime
import ta
import plotly.graph_objects as go
from Pages.Utils.Plotly import close_chart, plotly_table,RSI,Moving_average,MACD,candlestick
st.set_page_config(
    page_title="Stock Analysis",
    page_icon="chart_with_upwards_trend:",
    layout='wide'
)

st.title("Stock Analysis Section:chart_with_upwards_trend:")

col1,col2,col3 = st.columns(3)
today = datetime.date.today()
with col1:
    stock_symbol = st.text_input("Enter Stock Symbol",value='AAPL')
with col2:
    start_date = st.date_input("Start Date",value=datetime.date(today.year -1, today.month, today.day))
with col3:
    end_date = st.date_input("End Date",value=today)

st.subheader(stock_symbol)

stock = yf.Ticker(stock_symbol)

st.write(stock.info['longBusinessSummary'])
st.write(f"**Sector:** {stock.info['sector']}")
st.write(f"**Full Time Employees:** {stock.info['fullTimeEmployees']}")
st.write(f"**website:** {stock.info['website']}")

col1,col2 = st.columns(2)

with col1:
    df = pd.DataFrame(index=['Market Cap', 'Forward P/E', 'Enterprise Value/EBITDA','Beta'])
    df[' '] = [stock.info.get('marketCap'),
               stock.info.get('forwardPE'),
                stock.info.get('enterpriseToEbitda'),
                stock.info.get('beta')]
    st.plotly_chart(plotly_table(df),use_container_width=True)


with col2:
    df = pd.DataFrame(index=['quickRatio', 'revunuePerShare', 'debtToEquity','returnOnAssets','profit Margins'])
    df[' '] = [stock.info.get('quickRatio'),
               stock.info.get('revenuePerShare'),
                stock.info.get('debtToEquity'),
                stock.info.get('returnOnAssets'),
                stock.info.get('profitMargins')]
    st.plotly_chart(plotly_table(df),use_container_width=True)

data = yf.download(stock_symbol, start=start_date, end=end_date)

col1,col2,col3 = st.columns(3)

daily_change = data['Close'].iloc[-1] - data['Close'].iloc[-2]
col1.metric("Daily Change",str(round(data['Close'].iloc[-1],2)),str(round(daily_change,2)))

last_10_df = data.tail(10).sort_index(ascending=False).round(3)
fig_df = plotly_table(last_10_df)

st.write("### Last 10 Days Data Table")
st.plotly_chart(fig_df,use_container_width=True)

col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12 = st.columns(12)

num_period=''
with col1:
    if st.button("5D"):
        num_period = '5d'
with col2:
    if st.button("1M"):
        num_period = '1mo'
with col3:
    if st.button("3M"):
        num_period = '3mo'
with col4:
    if st.button("6M"):
        num_period = '6mo'
with col5:
    if st.button("YTD"):
        num_period = 'ytd'
with col6:
    if st.button("1Y"):
        num_period = '1y'   

with col7:
    if st.button("5Y"):
        num_period = '5y'

with col8:
    if st.button("MAX"):
        num_period = 'max'  

col1,col2,col3 = st.columns([1,1,4])
with col1:
    chart_type = st.selectbox(" ",options=['Line Chart','Candle Stick'])
with col2:
    if chart_type == 'Candle Stick':
        indicators = st.selectbox("",options=['RSI','MACD'])
    else:
        indicators = st.selectbox("",options=['moving Average','RSI','MACD'])

ticker = yf.Ticker(stock_symbol)
new_df_1 = ticker.history(period='max')
data1  = ticker.history(period='max')
if num_period == '':
    if chart_type == 'Candle Stick' and indicators == 'RSI':
        st.plotly_chart(candlestick(data1,'1y'),use_container_width=True)
        st.plotly_chart(RSI(data1,'1y'),use_container_width=True)
    if chart_type == 'Candle Stick' and indicators == 'MACD':
        st.plotly_chart(candlestick(data1,'1y'),use_container_width=True)
        st.plotly_chart(MACD(data1,'1y'),use_container_width=True)

    if chart_type == 'Line Chart' and indicators == 'RSI':
        st.plotly_chart(close_chart(data1,'1y'),use_container_width=True)
        st.plotly_chart(RSI(data1,'1y'),use_container_width=True)

    if chart_type == 'Line Chart' and indicators == 'moving Average':
        st.plotly_chart(close_chart(data1,'1y'),use_container_width=True)
        st.plotly_chart(Moving_average(data1,'1y'),use_container_width=True)

    if chart_type == 'Line Chart' and indicators == 'MACD':
        st.plotly_chart(close_chart(data1,'1y'),use_container_width=True)
        st.plotly_chart(MACD(data1,'1y'),use_container_width=True)
else:
    if chart_type == 'Candle Stick' and indicators == 'RSI':
        st.plotly_chart(candlestick(data1,num_period),use_container_width=True)
        st.plotly_chart(RSI(data1,num_period),use_container_width=True)
    if chart_type == 'Candle Stick' and indicators == 'MACD':
        st.plotly_chart(candlestick(data1,num_period),use_container_width=True)
        st.plotly_chart(MACD(data1,num_period),use_container_width=True)

    if chart_type == 'Line Chart' and indicators == 'RSI':
        st.plotly_chart(close_chart(data1,num_period),use_container_width=True)
        st.plotly_chart(RSI(data1,num_period),use_container_width=True)

    if chart_type == 'Line Chart' and indicators == 'moving Average':
        st.plotly_chart(close_chart(data1,num_period),use_container_width=True)
        st.plotly_chart(Moving_average(data1,num_period),use_container_width=True)

    if chart_type == 'Line Chart' and indicators == 'MACD':
        st.plotly_chart(close_chart(data1,num_period),use_container_width=True)
        st.plotly_chart(MACD(data1,num_period),use_container_width=True)    