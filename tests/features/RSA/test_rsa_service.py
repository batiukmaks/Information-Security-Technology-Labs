import unittest
from unittest.mock import patch

from features.RSA.rsa_service import RSAService


class TestRSAService(unittest.TestCase):

    @patch("builtins.input", create=True)
    def setUp(self, mock_input):
        mock_input.return_value = ""  # Default return value for input
        self.service = RSAService()

    def test_generate_key(self):
        self.service.generate_key()

        # Test that keys were actually generated
        self.assertIsNotNone(self.service.private_key)
        self.assertIsNotNone(self.service.public_key)

    @patch("builtins.input", side_effect=["Test message"])
    def test_encrypt_message(self, _):
        self.service.encrypt_message()

        # Test that encrypted message is not default 
        self.assertNotEqual(self.service.encrypted_message,
                            "There is no encrypted message yet. Use the menu to encrypt your message.")

    @patch("builtins.input", side_effect=["Test encrypted message"])
    def test_enter_encrypted_message(self, _):
        self.service.enter_encrypted_message()

        # Test that encrypted message changed
        self.assertEqual(self.service.encrypted_message, b"Test encrypted message")



if __name__ == "__main__":
    unittest.main()