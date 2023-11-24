from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives.asymmetric.dsa import DSAPrivateKey
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
import binascii


class DSS:
    def __init__(self):
        self.private_key = dsa.generate_private_key(key_size=1024)
        self.public_key = self.private_key.public_key()

    def create_signature(self, message: str) -> bytes:
        signature = self.private_key.sign(
            data=message.encode(),
            algorithm=hashes.SHA256()
        )
        return signature

    def verify_signature(self, message: str, signature: bytes) -> bool:
        try:
            self.public_key.verify(
                signature=signature,
                data=message.encode(),
                algorithm=hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False

    def create_hex_signature(self, message: str) -> str:
        signature = self.create_signature(message)
        hex_signature = binascii.hexlify(signature)
        return hex_signature.decode()

    def verify_hex_signature(self, message: str, hex_signature: str) -> bool:
        try:
            signature = binascii.unhexlify(hex_signature)
            return self.verify_signature(message, signature)
        except binascii.Error:
            return False

    # def create_file_signature(self, file_path: str) -> bytes:
    #     with open(file_path, "rb") as file:
    #         file_data = file.read()
    #         signature = self.create_signature(file_data)
    #         return signature


def main():
    # Ініціалізація DSS
    dss = DSS()

    # Підпис повідомлення
    message = "Hello, world!"
    signature = dss.create_signature(message)
    print(f"Message: {message}")
    print(f"Signature: {signature}")



if __name__ == "__main__":
    main()