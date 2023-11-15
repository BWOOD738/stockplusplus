"""
Author(s): BW,JP

Purpose: Provides functions to display stocks in a certain way
"""

from api import get_stock_data, top_tickers,start_date,end_date
import yfinance as yf
import pandas as pd

# TODO We should find a way to call the get_stock_data() function only once for all filter functions since it is a very expensive function.

 # This array is for testing so I don't have to download 100 stocks everytime
tickers = ["AAPL", "MSFT", "AMZN", "NVDA", "META"]

def order_by(stock_symbol) -> list:

    # NOTE Make sure to put "top_tickers" in the argument list below
    data = get_stock_data(tickers)
    # stick everything into an array
    data_array = [data]
    return sorted(data_array)

# Gets the market cap of the stocks. Just takes volume * price per share
def market_capitalization(stock_symbol):
    stocks = []
    
# This function is kinda messed up because it only allows you to get the yield for one stock at a time. The ticker symbol must also be single quotes. Some real fuckery is happening here.
def dividend_yield(stock_symbol):
    if not isinstance(stock_symbol, str):
        raise ValueError("Ticker symbol must be a string")

    # Download historical data for the given stock symbol. Probably should change the start and end dates 
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

    ticker = yf.Ticker(stock_symbol)
    
    try:
        dividends = ticker.dividends
    except AttributeError:
        # Handle the case where there are no dividends data
        print(f"No dividend data found for {stock_symbol}")
        return pd.DataFrame()

    return dividends



