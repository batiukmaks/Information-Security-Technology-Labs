import unittest
from unittest.mock import patch
from unittest.mock import Mock
from main import show_initial_options

class TestMain(unittest.TestCase):

    @patch('main.available_features', [ ("TestFeature", Mock()) for _ in range(3)])
    @patch('builtins.input', side_effect=[1,0])
    def test_show_initial_options(self, mock_input):
        value = show_initial_options()
        self.assertEqual(value, False)


if __name__ == "__main__":
    unittest.main()