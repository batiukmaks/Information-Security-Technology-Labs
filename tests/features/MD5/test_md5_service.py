from features.MD5.md5_service import MD5Service

import unittest
from unittest.mock import patch

class TestMD5Service(unittest.TestCase):
    def setUp(self):
        self.service = MD5Service()

    @patch("builtins.input", return_value="Hello Test")
    def test_update_message_from_terminal(self, input):
        self.service.update_message_from_terminal()
        self.assertEqual(self.service.message, "Hello Test")

    @patch("builtins.input", return_value="1")
    def test_get_available_features(self, input):
        self.service.get_available_features()
        self.assertTrue(len(self.service.get_available_features()) > 0)

    @patch("builtins.input", return_value="0")
    def test_show_initial_options_exit(self, input):
        self.assertFalse(self.service.show_initial_options())

if __name__ == '__main__':
    unittest.main()