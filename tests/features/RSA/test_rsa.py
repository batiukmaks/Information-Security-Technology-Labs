import unittest
from features.RSA.rsa import RSA


class RSATest(unittest.TestCase):
    def setUp(self):
        self.my_rsa = RSA()

    def test_key_generation(self):
        private_key, public_key = self.my_rsa.generate_key()

        # Test if the keys are not None
        self.assertIsNotNone(private_key)
        self.assertIsNotNone(public_key)

    def test_encryption_and_decryption(self):
        test_message = b'This is a test message'
        private_key, public_key = self.my_rsa.generate_key()

        # Test encryption
        encrypted_msg = self.my_rsa.encrypt(public_key, test_message)
        self.assertIsNotNone(encrypted_msg)

        # Test decryption
        decrypted_msg = self.my_rsa.decrypt(private_key, encrypted_msg)
        self.assertEqual(decrypted_msg, test_message)


if __name__ == "__main__":
    unittest.main()