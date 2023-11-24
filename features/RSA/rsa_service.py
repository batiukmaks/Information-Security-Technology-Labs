from features.RC5.rc5_cbc_pad import RC5CBCPad
from features.MD5.md5 import MD5
from .rsa import RSA
import os
import time

class RSAService:
    def __init__(self):
        self.md5_service = MD5()
        self.rc5 = RC5CBCPad(self.md5_service.hexdigest("Default key").encode('utf-8'))

        self.rsa = RSA()
        self.private_key, self.public_key = self.rsa.generate_key()
        self.encrypted_message = "There is no encrypted message yet. Use the menu to encrypt your message."
        self.decrypted_message = "There is no decrypted message yet. Use the menu to decrypt your message."

        print("Welcome to RSA")
        print("Use menu to encrypt/decrypt your message")


    def generate_key(self):
        print("Generating new keys...")
        self.private_key, self.public_key = self.rsa.generate_key()
        print("Keys generated successfully.")


    def encrypt_message(self):
        print("Encrypt the message")
        message = input("Enter message: ")
        self.encrypted_message = self.rsa.encrypt(self.public_key, message.encode('utf-8'))
        print("Message encrypted successfully.")

    def show_encrypted_message(self):
        print("Encrypted message is ", self.encrypted_message)

    def enter_encrypted_message(self):
        self.encrypted_message = input("Enter encrypted message: ").encode('utf-8')

    def decrypt_message(self):
        print("Decrypt the message...")
        self.decrypted_message = self.rsa.decrypt(self.private_key, self.encrypted_message)
        print("Message decrypted successfully.")

    def show_decrypted_message(self):
        print("Decrypted message is ", self.decrypted_message)

    def compare_encrypting_time(self):
        print("Compare encrypting time between RSA and RC5")
        message = input("Enter message: ")
        rsa_start_time = time.time()
        rsa_encrypted_message = self.rsa.encrypt(self.public_key, message.encode())
        rsa_end_time = time.time()
        rsa_time = rsa_end_time - rsa_start_time

        rc5_start_time = time.time()
        rc5_encrypted_message = self.rc5.encrypt(message.encode())
        rc5_end_time = time.time()
        rc5_time = rc5_end_time - rc5_start_time

        print("RSA time: ", rsa_time)
        print("RC5 time: ", rc5_time)
        if rsa_time < rc5_time:
            print("RSA is faster")
        elif rsa_time > rc5_time:
            print("RC5 is faster")
        else:
            print("RSA and RC5 are equally fast")



    def get_available_features(self):
        available_features = [
            ("Generate new keys", self.generate_key),
            ("Encrypt message", self.encrypt_message),
            ("Show encrypted message", self.show_encrypted_message),
            ("Enter encrypted message", self.enter_encrypted_message),
            ("Decrypt message", self.decrypt_message),
            ("Show decrypted message", self.show_decrypted_message),
            ("Compare encrypting time between RSA and RC5", self.compare_encrypting_time)
        ]
        return available_features


    def show_initial_options(self):
        available_features = self.get_available_features()
        while True:
            print("Choose the option:")
            for i in range(len(available_features)):
                print(f"{i + 1}. {available_features[i][0]}")
            print("0. Exit")

            try:
                option = int(input("Option: "))
                if option == 0:
                    return False

                print()
                available_features[option - 1][1]()
                input("Press Enter to continue...")
                os.system("clear")
            except Exception as e:
                print("ERROR: ", e)
                continue


def entry_point():
    service = RSAService()
    while True:
        if not service.show_initial_options():
            break





