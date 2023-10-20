
import os
import struct

from features.MD5.md5 import MD5
md5_service = MD5()


class RC5CBCPad:
    def __init__(self, key, block_size=8):
        self.key = self._pad_key(key, block_size)
        self.block_size = block_size

    def _pad_key(self, key, block_size):
        key_len = len(key)
        if key_len >= block_size:
            return key[:block_size]
        else:
            return key + b'\x00' * (block_size - key_len)

    def _xor_bytes(self, a, b):
        return bytes(x ^ y for x, y in zip(a, b))

    def _pad_data(self, data):
        padding_len = self.block_size - len(data) % self.block_size
        padding = bytes([padding_len] * padding_len)
        return data + padding

    def _unpad_data(self, data):
        padding_len = data[-1]
        if padding_len < 1 or padding_len > self.block_size:
            raise ValueError("Invalid padding")
        if data[-padding_len:] != bytes([padding_len] * padding_len):
            raise ValueError("Invalid padding")
        return data[:-padding_len]

    def _split_blocks(self, data):
        return [data[i:i + self.block_size] for i in range(0, len(data), self.block_size)]

    def encrypt(self, plaintext, iv):
        plaintext = self._pad_data(plaintext)
        blocks = self._split_blocks(plaintext)
        ciphertext = b''
        prev_block = iv

        for block in blocks:
            block = self._xor_bytes(block, prev_block)
            cipher = self._rc5_encrypt_block(block)
            ciphertext += cipher
            prev_block = cipher

        return iv + ciphertext

    def decrypt(self, ciphertext, iv):
        blocks = self._split_blocks(ciphertext[len(iv):])
        plaintext = b''
        prev_block = iv

        for block in blocks:
            decrypted_block = self._rc5_decrypt_block(block)
            plaintext += self._xor_bytes(decrypted_block, prev_block)
            prev_block = block

        plaintext = self._unpad_data(plaintext)
        return plaintext


    def _rc5_encrypt_block(self, block):
        # Implement a simplified version of RC5 encryption for a single block
        # This is not a secure RC5 implementation and is for educational purposes only
        word_size = 16  # RC5 word size in bits
        num_rounds = 12  # Number of RC5 rounds

        # Convert the block into four words (A, B, C, and D)
        A, B, C, D = struct.unpack('!HHHH', block)

        # Key expansion (you should implement a secure key expansion)
        round_keys = self._expand_key()

        # Perform encryption rounds
        for i in range(num_rounds):
            A = (A + round_keys[2 * i]) & ((1 << word_size) - 1)
            B = (B + round_keys[2 * i + 1]) & ((1 << word_size) - 1)
            A ^= B
            A = (A << (B % word_size)) | (A >> (word_size - (B % word_size)))
            A &= ((1 << word_size) - 1)

            C = (C + round_keys[2 * i]) & ((1 << word_size) - 1)
            D = (D + round_keys[2 * i + 1]) & ((1 << word_size) - 1)
            C ^= D
            C = (C << (D % word_size)) | (C >> (word_size - (D % word_size)))
            C &= ((1 << word_size) - 1)

        # Combine the four words into the ciphertext block
        return struct.pack('!HHHH', A, B, C, D)

    def _rc5_decrypt_block(self, block):
        # Implement a simplified version of RC5 decryption for a single block
        # This is not a secure RC5 implementation and is for educational purposes only
        word_size = 16  # RC5 word size in bits
        num_rounds = 12  # Number of RC5 rounds

        # Convert the block into four words (A, B, C, and D)
        A, B, C, D = struct.unpack('!HHHH', block)

        # Key expansion (you should implement a secure key expansion)
        round_keys = self._expand_key()

        # Perform decryption rounds in reverse order
        for i in range(num_rounds - 1, -1, -1):
            C = (C >> (D % word_size)) | (C << (word_size - (D % word_size)))
            C &= ((1 << word_size) - 1)
            C ^= D
            D = (D - round_keys[2 * i + 1]) & ((1 << word_size) - 1)
            C = (C - round_keys[2 * i]) & ((1 << word_size) - 1)

            A = (A >> (B % word_size)) | (A << (word_size - (B % word_size)))
            A &= ((1 << word_size) - 1)
            A ^= B
            B = (B - round_keys[2 * i + 1]) & ((1 << word_size) - 1)
            A = (A - round_keys[2 * i]) & ((1 << word_size) - 1)

        # Combine the four words into the plaintext block
        return struct.pack('!HHHH', A, B, C, D)

    def _expand_key(self):
        # This is a simplified key expansion function for educational purposes only
        word_size = 16  # RC5 word size in bits
        num_rounds = 12  # Number of RC5 rounds

        # Determine the number of key words based on the word size
        num_key_words = len(self.key) // (word_size // 8)

        # Initialize the expanded key with a constant P value and Q value
        P = 0xB7E15163
        Q = 0x9E3779B9
        round_keys = [(P + (i * Q)) & ((1 << word_size) - 1) for i in range(2 * (num_rounds + 1))]

        # Convert the user-provided key into a list of words
        key_words = list(struct.unpack('!' + 'H' * num_key_words, self.key))

        # Key expansion algorithm (simplified)
        i = j = 0
        A = B = 0
        for _ in range(3 * max(len(key_words), 2 * (num_rounds + 1))):
            A = round_keys[i] = (round_keys[i] + A + B) & ((1 << word_size) - 1)
            B = key_words[j] = (key_words[j] + A + B) & ((1 << word_size) - 1)
            i = (i + 1) % (2 * (num_rounds + 1))
            j = (j + 1) % len(key_words)

        return round_keys


    def encrypt_file(self, input_filename, output_filename):
        iv = os.urandom(8)

        with open(input_filename, 'rb') as infile:
            plaintext = infile.read()

        encrypted_data = self.encrypt(plaintext, iv)

        with open(output_filename, 'wb') as outfile:
            outfile.write(iv + encrypted_data)

        print("Encryption complete. Encrypted data saved to", output_filename)

    def decrypt_file(self, input_filename, output_filename):
        with open(input_filename, 'rb') as infile:
            iv_ciphertext = infile.read()

        iv = iv_ciphertext[:8]
        ciphertext = iv_ciphertext[8:]

        decrypted_data = self.decrypt(ciphertext, iv)

        with open(output_filename, 'wb') as outfile:
            outfile.write(decrypted_data)

        print("Decryption complete. Decrypted data saved to", output_filename)


if __name__ == "__main__":
    passphrase = input("Enter passphrase: ")
    key = md5_service.hexdigest(passphrase).encode('utf-8')
    rc5_cbc_pad = RC5CBCPad(key)

    while True:
        print("\nOptions:")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            input_file = input("Enter the name of the file to encrypt: ")
            output_file = input("Enter the name of the encrypted file: ")
            rc5_cbc_pad.encrypt_file(input_file, output_file)

        elif choice == '2':
            input_file = input("Enter the name of the encrypted file: ")
            output_file = input("Enter the name of the decrypted file: ")
            rc5_cbc_pad.decrypt_file(input_file, output_file)

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please choose a valid option.")