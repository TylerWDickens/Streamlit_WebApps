import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Stock Price Application

 Stock price closing price and volume of **Google** stock.
""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2015-1-01', end='2021-10-15')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
