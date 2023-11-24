import unittest
from features.DSS.dss import DSS


class TestDSS(unittest.TestCase):

    def setUp(self):
        self.dss = DSS()

    def test_verify_signature(self):
        message = "Hello, world!"
        signature = self.dss.create_signature(message)
        self.assertTrue(self.dss.verify_signature(message, signature))

    def test_verify_signature_invalid_signature(self):
        message = "Hello, world!"
        signature = b'this is a bad signature'
        self.assertFalse(self.dss.verify_signature(message, signature))

    def test_verify_hex_signature(self):
        message = "Hello, world!"
        hex_signature = self.dss.create_hex_signature(message)
        self.assertTrue(self.dss.verify_hex_signature(message, hex_signature))

    def test_verify_hex_signature_invalid_signature(self):
        message = "Hello, world!"
        hex_signature = "this is a bad signature"
        self.assertFalse(self.dss.verify_hex_signature(message, hex_signature))


if __name__ == "__main__":
    unittest.main()