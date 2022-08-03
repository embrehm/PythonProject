!pip install yfinance==0.1.67
#!pip install pandas==1.3.3

import yfinance as yf
import pandas as pd

# Ticker module - allows creation of data extraction object based on the ticker symbol for the stock provided. Below creates extraction object for apple.

extract_apple = yf.Ticker("AAPL")
 
# attribute info - extract info about stock as Python Dictionary
apple_info = extract_apple.info

# method - history - provides the share price of the stock over a certain period of time. Param - period - can set how far back from the present to get data, 1 day (1d), 1 month (1m), 1 year (1y), max. Data is returned in a Pandas DataFrame. Date is the index, Open, High, Low, Close, Volume, and Stock Splits are given for each Day.
apple_share_price_data = extract_apple.history(period="max")
apple_share_price_data.reset_index(inplace=True)

apple_share_price_data.plot(x="Date", y="Open")

# attribute dividends - dataframe of the the dividends for the period provided.
extract_apple.dividends.plot()
