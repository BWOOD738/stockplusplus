import unittest
from unittest.mock import patch, Mock
import pandas as pd
from filters import dividend_yield 

class TestDividendYieldFunction(unittest.TestCase):

    @patch('filters.yf.download')
    @patch('filters.yf.Ticker')
    def test_dividend_yield_with_valid_data(self, mock_ticker, mock_download):
        # Mock data for the stock symbol
        mock_dividends_data = pd.Series([0.5, 0.6, 0.7], index=pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01']))

        # Configure the mock objects
        mock_download.return_value = pd.DataFrame({'Open': [100, 105, 110], 'Close': [105, 110, 115]})
        mock_ticker.return_value.dividends = mock_dividends_data

        # Call the function with a valid stock symbol
        result = dividend_yield('AAPL')  

        # Assert that the result is as expected
        expected_result = mock_dividends_data
        pd.testing.assert_series_equal(result, expected_result)

if __name__ == '__main__':
    unittest.main()