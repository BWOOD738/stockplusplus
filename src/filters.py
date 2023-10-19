"""
Author(s): BW,JP

Purpose: Provides functions to display stocks in a certain way
"""

from api import get_stock_data, top_tickers

# TODO We should find a way to call the get_stock_data() function only once for all filter functions since it is a very expensive function.

def order_by() -> list:
    # This array is for testing so I don't have to download 100 stocks everytime
    tickers = ["AAPL", "MSFT", "AMZN", "NVDA", "META"]

    # NOTE Make sure to put "top_tickers" in the argument list below
    data = get_stock_data(tickers)
    # stick everything into an array
    data_array = [data]
    return sorted(data_array)

    


