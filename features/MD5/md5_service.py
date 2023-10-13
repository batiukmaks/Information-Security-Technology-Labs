from .md5 import MD5
import os

class MD5Service:
    def __init__(self):
        self.md5 = MD5()

        self.default_input_filepath = "/Users/batiukmaks/PycharmProjects/Information-Security-Technology-Labs/features/MD5/example-input.csv"

        self.input_filepath = self.default_input_filepath
        self.output_filepath = "/Users/batiukmaks/PycharmProjects/Information-Security-Technology-Labs/results/md5_results.txt"

        self.message = "Hello, world!"

        self.hashed_message = "There is no hash yet. Use the menu to hash your message/file."

        print("Welcome to MD5")
        print("Default parameters are:")
        print(f"Message: {self.message}\n")


    def update_message_from_terminal(self):
        print("Updating message from terminal")
        self.message = input("Message: ")
        print(f"Message is updated to {self.message}")


    def update_message_from_csv_file(self):
        print("Updating message from csv file")
        while True:
            print(f"Enter path to csv file with message or press Enter to use default file {self.input_filepath}")
            filepath = input("Path: ")
            if not filepath:
                filepath = self.input_filepath
            try:
                with open(filepath, "r") as file:
                    self.message = file.read()
                break
            except FileNotFoundError:
                print("File not found. Try again.")
        print(f"Message is updated to {self.message}")


    def get_file_for_hashing(self):
        print("Getting file for hashing")
        while True:
            print(f"Enter path to csv file with message or press Enter to use default file {self.input_filepath}")
            filepath = input("Path: ")
            if not filepath:
                filepath = self.input_filepath
            try:
                with open(filepath, "rb") as file:
                    self.message = file.read()
                break
            except FileNotFoundError:
                print("File not found. Try again.")
        print("Successfully read file")


    def hash_message(self):
        hashed = self.md5.hexdigest(self.message)
        self.hashed_message = hashed


    def print_hashed_message(self):
        print("Hashed message is ", self.hashed_message)


    def check_file_integrity(self):
        print("Checking file integrity")
        while True:
            print(f"Enter path to csv file with message or press Enter to use default file {self.input_filepath}")
            filepath = input("Path: ")
            if not filepath:
                filepath = self.input_filepath
            try:
                with open(filepath, "rb") as file:
                    self.message = file.read()
                break
            except FileNotFoundError:
                print("File not found. Try again.")

        while True:
            print("Enter expected hash")
            expected_hash = input("Hash: ")
            if not expected_hash:
                print("Expected hash is empty. Try again.")
            else:
                break

        actual_hash = self.md5.hexdigest(self.message)
        print(f"Actual hash is {actual_hash}")
        if actual_hash == expected_hash:
            print("Hashes are equal. File is not corrupted.")
            self.hashed_message = "Hashes are equal. File is not corrupted."
        else:
            print("Hashes are not equal. File is corrupted.")
            self.hashed_message = "Hashes are not equal. File is corrupted."



    def save_to_file(self):
        print("Saving to file")
        while True:
            print("Enter path to output file or press Enter to use default file:", self.output_filepath)
            filepath = input("Path: ")
            if not filepath:
                filepath = self.output_filepath
            break

        with open(filepath, "w") as file:
            file.write(self.hashed_message)
        print(f"Hashed message is saved to {filepath}")


    def get_available_features(self):
        available_features = [
            ("Set message from terminal", self.update_message_from_terminal),
            ("Set message from csv file", self.update_message_from_csv_file),
            ("Set file as message for hashing", self.get_file_for_hashing),
            ("Hash current message", self.hash_message),
            ("Check file integrity", self.check_file_integrity),
            ("Save to file", self.save_to_file),
            ("Print hashed message", self.print_hashed_message),
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
            except:
                continue


def entry_point():
    service = MD5Service()
    while True:
        if not service.show_initial_options():
            break





