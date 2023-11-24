import unittest
from unittest.mock import patch

from features.RC5.rc5_service import RC5_CBC_PADSERVICE


class TestRC5_CBC_PADSERVICE(unittest.TestCase):

    @patch("features.RC5.rc5_service.RC5_CBC_PADSERVICE.input", create=True)
    @patch("os.path.exists")
    @patch("features.RC5.rc5_service.RC5CBCPad", autospec=True)
    def setUp(self, mock_rc5cbcpad, mock_exists, mock_input):
        mock_input.return_value = ""
        mock_exists.return_value = True
        mock_rc5cbcpad.return_value.encrypt_file.return_value = None
        mock_rc5cbcpad.return_value.decrypt_file.return_value = None
        self.service = RC5_CBC_PADSERVICE()

    def test_get_available_features(self):
        length = len(self.service.get_available_features())
        self.assertEqual(length, 2)

if __name__ == "__main__":
    unittest.main()