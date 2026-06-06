import streamlit as st
import pandas as pd
import yfinance as yf

from ta.momentum import RSIIndicator
from ta.trend import MACD
from prophet import Prophet

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="Stock Market Analytics Platform",
    layout="wide"
)

# ==================================
# SIDEBAR
# ==================================

st.sidebar.title("📊 Dashboard Menu")

st.sidebar.info(
    """
    Stock Market Analytics Platform

    Features:
    - Technical Indicators
    - Machine Learning Analysis
    - Forecasting
    - Risk Analysis
    """
)

# ==================================
# PROPHET CACHE
# ==================================

@st.cache_resource
def train_prophet(data):

    prophet_df = data.reset_index()[["Date", "Close"]]

    prophet_df.columns = [
        "ds",
        "y"
    ]

    model = Prophet()

    model.fit(prophet_df)

    future = model.make_future_dataframe(
        periods=30
    )

    forecast = model.predict(future)

    return forecast

# ==================================
# TITLE
# ==================================

st.title("📈 Stock Market Analytics Platform")
st.write("Machine Learning & Forecasting Dashboard")

# ==================================
# STOCK SELECTOR
# ==================================

ticker = st.selectbox(
    "Select Stock",
    ["AAPL", "TSLA", "MSFT", "GOOGL"]
)

# ==================================
# DOWNLOAD DATA
# ==================================

df = yf.download(
    ticker,
    start="2018-01-01",
    end="2025-01-01"
)

# Fix MultiIndex issue
df.columns = df.columns.get_level_values(0)

# ==================================
# TECHNICAL INDICATORS
# ==================================

# RSI
df["RSI"] = RSIIndicator(
    close=df["Close"],
    window=14
).rsi()

# MACD
macd = MACD(df["Close"])

df["MACD"] = macd.macd()

# Daily Return
df["Return"] = df["Close"].pct_change()

# Volatility
volatility = df["Return"].std()

# ==================================
# TOP METRICS
# ==================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Random Forest Accuracy",
        "52.97%"
    )

with col2:
    st.metric(
        "XGBoost Accuracy",
        "48.98%"
    )

with col3:
    st.metric(
        "Forecast Horizon",
        "30 Days"
    )

with col4:
    st.metric(
        "Volatility",
        round(volatility, 4)
    )

# ==================================
# LATEST PRICE
# ==================================

latest_price = round(
    float(df["Close"].iloc[-1]),
    2
)

st.metric(
    f"{ticker} Latest Price",
    f"${latest_price}"
)

# ==================================
# RISK LEVEL
# ==================================

if volatility < 0.015:
    risk = "🟢 Low Risk"

elif volatility < 0.03:
    risk = "🟡 Medium Risk"

else:
    risk = "🔴 High Risk"

st.metric(
    "Risk Level",
    risk
)

# ==================================
# TRADING SIGNAL
# ==================================

latest_rsi = df["RSI"].iloc[-1]

st.subheader("🚦 Trading Signal")

if latest_rsi < 30:
    st.success("🟢 BUY Signal")

elif latest_rsi > 70:
    st.error("🔴 SELL Signal")

else:
    st.info("🟡 HOLD Signal")

# ==================================
# DATASET PREVIEW
# ==================================

with st.expander("📋 View Dataset Preview"):
    st.dataframe(df.head(20))

# ==================================
# PRICE CHART
# ==================================

st.header(f"📈 {ticker} Closing Price (Last 1 Year)")

st.line_chart(
    df["Close"].tail(252)
)

# ==================================
# RSI CHART
# ==================================

st.header("📊 RSI Indicator")

st.line_chart(
    df["RSI"].tail(252)
)

# ==================================
# MACD CHART
# ==================================

st.header("📊 MACD Indicator")

st.line_chart(
    df["MACD"].tail(252)
)

# ==================================
# PROPHET FORECAST
# ==================================

forecast = train_prophet(df)

forecast_price = round(
    forecast["yhat"].iloc[-1],
    2
)

forecast_lower = round(
    forecast["yhat_lower"].iloc[-1],
    2
)

forecast_upper = round(
    forecast["yhat_upper"].iloc[-1],
    2
)

# ==================================
# FORECAST SUMMARY
# ==================================

st.header("🔮 Forecast Summary")

st.write(
    """
    Prophet forecasting model predicts future stock trends
    using historical market data and seasonality patterns.
    """
)

st.metric(
    "30-Day Forecast Price",
    f"${forecast_price}"
)

st.write(
    f"Expected Price Range: ${forecast_lower} - ${forecast_upper}"
)

# ==================================
# FORECAST CHART
# ==================================

st.header("🔮 Prophet Forecast Chart")

forecast_chart = forecast.set_index("ds")

st.line_chart(
    forecast_chart["yhat"].tail(365)
)

# ==================================
# PROJECT SUMMARY
# ==================================

st.header("📑 Project Summary")

st.write(
    """
    This project combines:

    ✅ Random Forest Classification

    ✅ XGBoost Classification

    ✅ Prophet Forecasting

    ✅ RSI Analysis

    ✅ MACD Analysis

    ✅ Volatility Analysis

    ✅ Technical Indicator Engineering

    to analyze stock behavior and generate actionable insights.
    """
)