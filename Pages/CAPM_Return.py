import streamlit as st 
import pandas as pd
import yfinance as yf
import datetime
import pandas_datareader.data as web

import CAPM_functions as CAPM_functions

st.set_page_config(page_title = "CAPM",page_icon="Chart_with_Upwards_trend",layout = 'wide')

st.title("Capital Assets Pricing Model")
col1,col2 = st.columns([1,1])
with col1:
    stock_data = st.multiselect("Choose 4 Stocks from the below",('TSLA','AAPL','MSFT','NFLX','AMZN','NVDA','GOOGL'),['TSLA','AAPL','MSFT','NVDA'])
with col2:
    year = st.number_input("enter the o.of years",1,10)

end = datetime.date.today()
start = datetime.date(datetime.date.today().year-year,datetime.date.today().month,datetime.date.today().day)
sp500= pd.DataFrame()
sp500 = web.DataReader('SP500','fred',start,end)

# print(sp500)

stock_df = pd.DataFrame()

for stock in stock_data:
    data = yf.download(stock,period=f'{year}y')
    stock_df[f'{stock}'] = data['Close']
# sp500.columns = ['Date','SP500']
# sp500 = sp500.to_frame(name='SP500')
# print(stock_df)
# stock_df.dropna(inplace=True)
# stock_df.reset_index(drop=True, inplace=True)

sp500.reset_index(inplace=True)
stock_df.reset_index(inplace = True)
stock_df.rename(columns={stock_df.columns[0]: 'Date'}, inplace=True)
sp500.rename(columns={sp500.columns[0]: 'Date'}, inplace=True)
stock_df['Date'] = pd.to_datetime(stock_df['Date'])
sp500['Date'] = pd.to_datetime(sp500['Date'])


# print(stock_df.dtypes)
# print(sp500.dtypes)
stock_df = pd.merge(stock_df,sp500,how='inner',on='Date')
# print(stock_df)

col1,col2 = st.columns([1,1])

with col1:
    st.markdown("### DataFrame Head")
    st.dataframe(stock_df.head(),use_container_width = True)
with col2:
    st.markdown("### DataFrame Tail")
    st.dataframe(stock_df.tail(),use_container_width = True)

col1,col2 = st.columns([1,1])

with col1:
    st.markdown("### Price of All Stocks")
    st.plotly_chart(CAPM_functions.interactive_plot(stock_df))
with col2:
    st.markdown("### Price of All Stocks(Normalize)")
    st.plotly_chart(CAPM_functions.interactive_plot(CAPM_functions.Normalize(stock_df)))

stock_daily_returns = CAPM_functions.Daily_returns(stock_df)
print(stock_daily_returns)
beta = {}
alpha ={}

for i in stock_daily_returns.columns:
    if i != 'Date' and i != 'sp500':
        b,a = CAPM_functions.calculate_beta(stock_daily_returns,i)

        beta[i] = b
        alpha[i] = a
print(beta,alpha)
beta_df = pd.DataFrame(columns=['Stock','Beta Value'])
beta_df['Stock'] = beta.keys()
beta_df['Beta Value'] = [str(round(i,2)) for i in beta.values()]

col1,col2 = st.columns([1,1])

with col1:
    st.markdown("### Calculated Beta Value")
    st.dataframe(beta_df,use_container_width=True)

rf = 0
rm = stock_daily_returns['SP500'].mean()*252

return_df = pd.DataFrame()

return_value = []

for stock,value in beta.items():
    return_value.append(str(round(rf+value*(rm-rf),2)))

return_df['Stock'] = beta.keys()

return_df['Return Value'] = return_value

with col2:
    st.markdown("### Calculated Return Using CAPM")
    st.dataframe(return_df,use_container_width=True)

    