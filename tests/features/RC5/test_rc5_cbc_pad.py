import unittest
from features.RC5.rc5_cbc_pad import RC5CBCPad

class TestRC5CBCPad(unittest.TestCase):
    def setUp(self):
        key = b"This is key1234"
        self.rc5 = RC5CBCPad(key)

    def test_encrypt_decrypt(self):
        plaintext = b"This is some text to test the RC5 algorithm."
        iv = b"12345678"
        ciphertext = self.rc5.encrypt(plaintext, iv)
        decrypted = self.rc5.decrypt(ciphertext, iv)
        self.assertEqual(plaintext, decrypted)

    def test_pad_unpad_data(self):
        data = b"Some data to be padded"
        padded = self.rc5._pad_data(data)
        unpadded = self.rc5._unpad_data(padded)
        self.assertEqual(data, unpadded)

    # Test encrypt_file and decrypt_file methods
    def test_encrypt_decrypt_file(self):
        input_filename = '/Users/batiukmaks/PycharmProjects/Information-Security-Technology-Labs/tests/features/RC5/test_in.txt'
        output_enc_filename = '/Users/batiukmaks/PycharmProjects/Information-Security-Technology-Labs/tests/features/RC5/test_enc.txt'
        output_dec_filename = '/Users/batiukmaks/PycharmProjects/Information-Security-Technology-Labs/tests/features/RC5/test_dec.txt'
        self.rc5.encrypt_file(input_filename, output_enc_filename)
        self.rc5.decrypt_file(output_enc_filename, output_dec_filename)

        # Now compare the initial file and decrypted file
        with open(input_filename, 'r') as f_initial:
            initial_content = f_initial.read()

        with open(output_dec_filename, 'r') as f_decrypted:
            decrypted_content = f_decrypted.read()

        self.assertEqual(initial_content, decrypted_content)

if __name__ == '__main__':
    unittest.main()