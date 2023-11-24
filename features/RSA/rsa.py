from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding as sym_padding

class RSA:
    def __init__(self):
        self.private_key, self.public_key = self.generate_key()

    def generate_key(self):
        # Генерація пари ключів RSA
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_key = private_key.public_key()
        return private_key, public_key

    def encrypt(self, public_key, plaintext):
        # Генерація випадкового ключа AES
        aes_key = Fernet.generate_key()

        # Шифрування повідомлення за допомогою AES
        f = Fernet(aes_key)
        ciphertext = f.encrypt(plaintext)

        # Шифрування ключа AES за допомогою RSA
        encrypted_aes_key = public_key.encrypt(
            aes_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return encrypted_aes_key + ciphertext

    def decrypt(self, private_key, encrypted):
        # Розшифровка ключа AES
        encrypted_aes_key, ciphertext = encrypted[:256], encrypted[256:]
        aes_key = private_key.decrypt(
            encrypted_aes_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        # Розшифровка повідомлення за допомогою AES
        f = Fernet(aes_key)
        plaintext = f.decrypt(ciphertext)

        return plaintext


if __name__ == '__main__':
    rsa_encription = RSA()
    private_key, public_key = rsa_encription.generate_key()
    message = b'Hello, World!'
    encrypted = rsa_encription.encrypt(public_key, message)
    decrypted = rsa_encription.decrypt(private_key, encrypted)
    print('Message:', message)
    print('Encrypted:', encrypted)
    print('Decrypted:', decrypted)