import streamlit as st
import yfinance as yf

df = yf.download("^GSPC")["Adj Close"]

st.line_chart(df)
