import os

from .rc5_cbc_pad import RC5CBCPad
from features.MD5.md5 import MD5


class RC5_CBC_PADSERVICE():
    def __init__(self):
        self.md5_service = MD5()
        self.input_file = '/Users/batiukmaks/PycharmProjects/Information-Security-Technology-Labs/features/RC5/example-input.txt'
        self.output_file = '/Users/batiukmaks/PycharmProjects/Information-Security-Technology-Labs/results/rc5_result.txt'

        self.word_size = 16
        self.num_rounds = 12
        self.passcode = "Default passcode"
        self.key = self.md5_service.hexdigest(self.passcode).encode('utf-8')
        self.service = RC5CBCPad(self.key, self.word_size, self.num_rounds)

        print("Welcome to RC5-CBC-Pad")
        print("Default parameters are:")
        print(f"Word size: {self.word_size}")
        print(f"Number of rounds: {self.num_rounds}")
        print(f"Passcode: {self.passcode}")
        print(f"Input file: {self.input_file}")
        print(f"Output file: {self.output_file}")
        print("You can change parameters in the menu")
        print()


    def update_params(self):
        print("Updating parameters")

        while True:
            try:
                new_pass = input("Enter new key: ")
                word_size = int(input("Enter new word size: "))
                num_rounds = int(input("Enter new number of rounds: "))
                key = self.md5_service.hexdigest(new_pass).encode('utf-8')


                self.key = key
                self.word_size = word_size
                self.num_rounds = num_rounds

                service = RC5CBCPad(self.key, self.word_size, self.num_rounds)
                self.service = service
                break
            except:
                continue

        print("Parameters updated successfully")


    def encrypt(self):
        print("Encrypting file")
        input_file_path = input(f"Enter input file path or press Enter to use default file {self.input_file}: ")
        if not input_file_path or not os.path.exists(input_file_path):
            input_file_path = self.input_file

        output_file_path = input(f"Enter output file path or press Enter to use default file {self.output_file}: ")
        if not output_file_path:
            output_file_path = self.output_file

        self.service.encrypt_file(input_file_path, output_file_path)

        print("Encryption complete. Encrypted data saved to", output_file_path)


    def decrypt(self):
        print("Decrypting file")
        input_file_path = input(f"Enter input file path or press Enter to use default file {self.output_file}: ")
        if not input_file_path or not os.path.exists(input_file_path):
            input_file_path = self.output_file

        output_file_path = input(f"Enter output file path or press Enter to use default file {self.input_file}: ")
        if not output_file_path:
            output_file_path = self.input_file

        self.service.decrypt_file(input_file_path, output_file_path)

        print("Decryption complete. Decrypted data saved to", output_file_path)

    def get_available_features(self):
        available_features = [
            ("Update parameters", self.update_params),
            ("Encrypt file", self.encrypt),
            ("Decrypt file", self.decrypt),
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
                print(e)
                continue

def entry_point():
    service = RC5_CBC_PADSERVICE()
    while True:
        if not service.show_initial_options():
            break
