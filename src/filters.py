"""
Author(s): BW

Purpose: Provides functions to display stocks in a certain way
"""

from api import get_stock_data,start_date,end_date
import yfinance as yf
import pandas as pd

 # This array is for testing so I don't have to download 100 stocks everytime
tickers_ = ["AAPL", "MSFT", "AMZN", "NVDA", "META"]

def order_by(tickers) -> list:

    # NOTE Make sure to put "top_tickers" in the argument list below
    data = get_stock_data(tickers)
    # stick everything into an array
    data_array = [data]
    return sorted(data_array)

# Gets the market cap of a stock. Just takes volume * price per share
def market_capitalization(stock_symbol):
    try:
        ticker = yf.Ticker(stock_symbol)
        todays_data = ticker.history(period='1d')

        price = todays_data['Close'].iloc[0]
        volume = todays_data['Volume'].iloc[0]

        return price * volume
    except Exception as e:
        print(f"Error getting market cap for {stock_symbol}: {e}")

def moving_average(stock_symbol, window_size=10):
    try:
        data = yf.Ticker(stock_symbol)
        close_prices = data.history(period='1mo')['Close']
        ma = close_prices.rolling(window=window_size).mean()
        last_ma_value = ma.iloc[-1]
        return last_ma_value
    except Exception as e:
        print(f"Error getting mean average for {stock_symbol}: {e}")



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