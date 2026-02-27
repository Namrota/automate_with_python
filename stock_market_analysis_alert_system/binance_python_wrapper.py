"""
THE APP:
Stock price tracker that fetches real-time data for multiple stock tickers
using API and displays it in a formatted table.

WHAT TO FIGURE OUT:
- How do you fetch stock data from an API?
- How do you extract specific fields from stock info?
- How do you calculate price changes and percentages?
- How do you format numbers (currency, percentages)?
- How do you format large numbers (millions, billions)?

START HERE:
First, get ticker symbols from the user and split them.
Then fetch data for each ticker using yfinance.
Finally, format and display the data in a clean table.

KEY CONCEPT:
Use yf.Ticker(symbol) to create a stock object.
Use .info to get a dictionary of stock data.
Calculate change: current_price - previous_close.
Calculate change%: (change / previous_close) * 100.
Format large numbers: divide by 1M, 1B, 1T and add suffix.
"""

#Import necessary libraries
import pandas as pd
from dotenv import load_dotenv
import os
from binance.client import Client

load_dotenv() # Load environment variables from local .env file
# Print header
print("App: Crypto Price Tracker and Alert System")
print("="*40)
# sample test: Get all tickers from binance testnet
api_key= os.environ['BINANCE_API_KEY_TEST']
api_secret= os.environ['BINANCE_API_SECRET_TEST']
client = Client(api_key, api_secret, testnet= True)
tickers= client.get_all_tickers()
print(tickers)
# Print status message


# Create empty list to store stock data