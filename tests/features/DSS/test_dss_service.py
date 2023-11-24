import unittest
from unittest.mock import patch
from features.DSS.dss_service import DSSService

class TestDSSService(unittest.TestCase):

    def setUp(self):
        self.service =  DSSService()

    def test_create_signature(self):
        self.service.message = "Test message"
        self.service.create_signature()
        self.assertIsInstance(self.service.hex_signature, str)
        self.assertNotEqual(self.service.hex_signature, "There is no signature yet.")

    @patch('os.path.exists', return_value=False)
    def test_read_file_path_not_exist(self, mock_exists):
        with patch('builtins.input', return_value="nonexistent.file"), self.assertRaises(Exception):
            self.service.read_file()

    def test_show_signature(self):
        self.service.message = "Test message"
        self.service.create_signature()
        with patch('builtins.print') as prnt:
            self.service.show_signature()
            prnt.assert_called_with("Signature: ", self.service.hex_signature)

if __name__ == "__main__":
    unittest.main()