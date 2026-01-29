import plotly.express as ex
import numpy as np
def interactive_plot(df):
    fig =ex.line()
    for i in df.columns[1:]:
        fig.add_scatter(x=df['Date'],y= df[i],name=i)

    fig.update_layout(width = 450,margin=dict(l=23,r=20,t=50,b=20),
                      legend=dict(orientation='h',yanchor='bottom',y=1.02,xanchor='right',x=1,))
    return fig

def Normalize(df_2):
    df = df_2.copy()
    for i in df.columns[1:]:
        df[i]=df[i]/df[i][0]
    return df

# def Daily_returns(df):
#     df_daily_returns = df.copy()
#     for i in df.columns[1:]:
#         for j in range(1,len(df)):
#             df_daily_returns[i][j]=((df[i][j]-df[i][j-1])/(df[i][j-1]))*100
#         df_daily_returns[i][0] = 0

#     return df_daily_returns
def Daily_returns(df):
    df_daily_returns = df.copy()

    for col in df.columns[1:]:
        df_daily_returns.loc[0, col] = 0
        for i in range(1, len(df)):
            df_daily_returns.loc[i, col] = (
                (df.loc[i, col] - df.loc[i-1, col]) / df.loc[i-1, col]
            ) * 100

    return df_daily_returns

def calculate_beta(stock_daily_returns,stock):
    rm = stock_daily_returns['SP500'].mean()*252

    b,a = np.polyfit(stock_daily_returns['SP500'],stock_daily_returns[stock],1)
    return b,a