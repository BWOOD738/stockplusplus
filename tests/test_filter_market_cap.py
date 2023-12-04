import unittest
from unittest.mock import MagicMock, patch
from filters import market_capitalization  

class TestMarketCapitalizationFunction(unittest.TestCase):

    @patch('filters.yf.Ticker')
    def test_market_capitalization_successful(self, mock_ticker):
        # Mocking the return value of the yf.Ticker().history() method
        mock_history = MagicMock()
        mock_history['Close'] = [100] 
        mock_history['Volume'] = [1000000]  
        mock_ticker.return_value.history.return_value = mock_history

        # Calling the function with a mocked Ticker instance
        result = market_capitalization("AAPL") 

        # Asserting the result
        self.assertEqual(result, 100000000) 
    @patch('filters.yf.Ticker')
    def test_market_capitalization_exception_handling(self, mock_ticker):
        # Mocking an exception when calling yf.Ticker()
        mock_ticker.side_effect = Exception("Mocked error")

        # Calling the function with a mocked Ticker instance
        result = market_capitalization("AAPL") 

        # Asserting that the function returns None when an exception occurs
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()