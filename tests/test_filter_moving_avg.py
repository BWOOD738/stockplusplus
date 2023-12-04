import unittest
from unittest.mock import MagicMock, patch
from filters import moving_average

class TestMovingAverageFunction(unittest.TestCase):

    @patch('filters.yf.Ticker')
    def test_moving_average_successful(self, mock_ticker):
        # Mocking the return value of the yf.Ticker().history() method
        mock_history = MagicMock()
        mock_history['Close'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
        mock_ticker.return_value.history.return_value = mock_history

        # Calling the function with a mocked Ticker instance
        result = moving_average("AAPL", window_size=3)  

        # Asserting the result
        self.assertEqual(result, 7.0)

    @patch('filters.yf.Ticker')
    def test_moving_average_exception_handling(self, mock_ticker):
        # Mocking an exception when calling yf.Ticker()
        mock_ticker.side_effect = Exception("Mocked error")

        # Calling the function with a mocked Ticker instance
        result = moving_average("AAPL", window_size=3) 

        # Asserting that the function returns None when an exception occurs
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()