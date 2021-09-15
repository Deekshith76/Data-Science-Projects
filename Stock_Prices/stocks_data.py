import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
         # Simple Stock Price App
         
         Shown are the stock **closing price** and ***volume*** of Google!
         """)

# one hash means header 1
# ** before and after a word --> bold
# *** before and after a word --> bold and italic

#define the ticker symbol
#ticker symbol for 'AAPL'
tickerSymbol  = 'GOOGL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# the Df comprises of Open High Low Close Volume Dividends Stock Splits

st.write("""
         ## **Open Price**
         """)
st.line_chart(tickerDf.Open)

st.write("""
         ## **Close Price**
         """)
st.line_chart(tickerDf.Close)
st.write("""
         ## **Volume Price**
         """)
st.line_chart(tickerDf.Volume)
st.write("""
         ## **High Value**
         """)
st.line_chart(tickerDf.High)
st.write("""
         ## **Low Value**
         """)
st.line_chart(tickerDf.Low)