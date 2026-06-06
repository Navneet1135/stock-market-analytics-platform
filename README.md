# 📈 Stock Market Analytics Platform

## Overview

The Stock Market Analytics Platform is an end-to-end Data Science and Machine Learning project designed to analyze stock market behavior, generate trading insights, and forecast future stock prices.

The platform combines technical analysis, machine learning models, and time-series forecasting into an interactive Streamlit dashboard.

Users can select a stock, analyze its performance, view technical indicators, assess risk, and generate future price forecasts.

---

## Features

### 📊 Technical Analysis

- Relative Strength Index (RSI)
- Moving Average Convergence Divergence (MACD)
- Daily Returns
- Volatility Analysis

### 🤖 Machine Learning

- Random Forest Classification
- XGBoost Classification

### 🔮 Forecasting

- Prophet Time-Series Forecasting
- 30-Day Stock Price Prediction
- Forecast Confidence Range

### 📈 Interactive Dashboard

- Multiple Stock Selection
- Latest Price Tracking
- Trading Signals (Buy / Hold / Sell)
- Risk Assessment
- Forecast Visualization

---

## Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- YFinance
- Scikit-Learn
- XGBoost
- Prophet
- TA (Technical Analysis)
- Streamlit
- Matplotlib

---

## Project Workflow

### 1. Data Collection

Historical stock market data is collected using Yahoo Finance using the YFinance library.

### 2. Exploratory Data Analysis (EDA)

- Price Trend Analysis
- Daily Returns Analysis
- Moving Averages
- Volatility Analysis

### 3. Feature Engineering

Technical indicators were generated including:

- RSI
- MACD
- Daily Returns
- Volatility

### 4. Machine Learning Models

Two machine learning models were trained:

- Random Forest Classifier
- XGBoost Classifier

### 5. Forecasting

Facebook Prophet was used to forecast future stock prices and estimate future trends.

### 6. Dashboard Development

A Streamlit dashboard was developed to provide:

- Stock Analysis
- Technical Indicators
- Risk Metrics
- Forecast Visualization

---

## Dashboard Features

### Overview

- Latest Stock Price
- Risk Level
- Forecast Horizon

### Technical Indicators

- RSI Chart
- MACD Chart

### Trading Signals

- Buy Signal
- Hold Signal
- Sell Signal

### Forecasting

- Forecast Price
- Confidence Range
- Forecast Trend Chart

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Navneet1135/stock-market-analytics-platform.git
```

### Move to Project Folder

```bash
cd stock-market-analytics-platform
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Dashboard

```bash
streamlit run app.py
```

---

## Project Structure

```text
stock-market-analytics-platform/

│
├── app.py
├── requirements.txt
├── README.md
├── stock_market_analysis.ipynb
└── screenshots/
```

---

## Future Improvements

- Candlestick Charts
- Real-Time Market Data
- News Sentiment Analysis
- Deep Learning Models (LSTM)
- Portfolio Optimization
- Advanced Trading Strategies

---

## Author

Navneet Pal
