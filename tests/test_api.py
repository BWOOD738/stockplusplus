"""
Author: BW
Purpose: Unit test of the get_stock_data function. Will make sure we return expected values.
"""

import unittest
from unittest.mock import patch, Mock
import pandas as pd
import yfinance as yf
from api import get_stock_data

class TestGetStockData(unittest.TestCase):

    @patch('yfinance.download')
    def test_get_stock_data(self, mock_download):
        # defining inputs and expected outputs
        top_tickers = ['AAPL', 'GOOGL']
        start_date = '2023-01-01'
        end_date = '2023-01-10'
        
        # Create mock dataframes to simulate the yfinance API responses
        mock_dataframes = {
            'AAPL': pd.DataFrame({
                'Close': [150.0, 151.0, 152.0],
                'Volume': [1000000, 1100000, 1200000],
            }),
            'GOOGL': pd.DataFrame({
                'Close': [2500.0, 2550.0, 2600.0],
                'Volume': [500000, 550000, 600000],
            })
        }
        
        mock_download.side_effect = lambda symbol, start, end: mock_dataframes[symbol]

        expected_columns = pd.MultiIndex.from_product([top_tickers, ["Close", "Volume"]],
                                                     names=["Ticker Symbol", "Attributes"])

        # Calling function
        stock_data = get_stock_data(top_tickers, start_date, end_date)
        
        # Check if the API was called with the expected arguments
        expected_calls = [((ticker, start_date, end_date),) for ticker in top_tickers]
        mock_download.assert_has_calls(expected_calls)
        
        # Check if the function returned the expected result
        self.assertTrue(stock_data.equals(expected_columns))

if __name__ == '__main__':
    unittest.main()