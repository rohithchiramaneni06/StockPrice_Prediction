import streamlit as st
from Pages.Utils.Models import get_data,get_differencing_order,get_rolling_mean,scaling,get_forecast,inverse_scaling,evaluate_model
import pandas as pd
from Pages.Utils.Plotly import Moving_average, plotly_table,Moving_average_forecast

st.set_page_config(
    page_title="Stock Price Prediction",
    page_icon="chart_with_upwards_trend:",
    layout='wide'
)

st.title("Stock Price Prediction Section:chart_with_upwards_trend:")

col1,col2,col3 = st.columns(3)

with col1:
    ticker = st.text_input("Enter Stock Ticker",value='AAPL')

rmse = 0
st.subheader(f"Stock Price Prediction for {ticker}")

close_price = get_data(ticker)
rolling_price = get_rolling_mean(close_price)

differencing_price = get_differencing_order(close_price)
scaled_data, scaler = scaling(close_price)
rmse = evaluate_model(close_price, differencing_price)

st.write(f"**Root Mean Squared Error (RMSE) of the Model:** {rmse}")

forecast = get_forecast(scaled_data, differencing_price)

forecast['Close'] = inverse_scaling(scaler, forecast['Close'])
st.write("### Forecasted Stock Prices for Next 30 Days")
fig_tail = plotly_table(forecast.sort_index(ascending=True).round(2))
fig_tail.update_layout(height=400)
st.plotly_chart(fig_tail, use_container_width=True)

forecast = pd.concat([rolling_price,forecast])

st.plotly_chart(Moving_average_forecast(forecast.iloc[150:]), use_container_width=True)