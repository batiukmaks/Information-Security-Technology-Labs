from .dss import DSS
import os

class DSSService:
    def __init__(self):
        self.dss = DSS()

        self.message = "There is no message yet."
        self.hex_signature = "There is no signature yet."

    def set_message(self):
        print("Setting message.")
        self.message = input("Enter message: ")
        print("Message is set.")

    def set_signature(self):
        print("Setting signature.")
        self.hex_signature = input("Enter signature: ")
        print("Signature is set.")

    def create_signature(self):
        self.hex_signature = self.dss.create_hex_signature(self.message)
        print("Signature is created.")

    def verify_signature(self):
        print("Verifying signature...")
        is_verified = self.dss.verify_hex_signature(self.message, self.hex_signature)
        if is_verified:
            print("Signature is verified =)")
        else:
            print("Signature is not verified =(")


    def read_file(self):
        file_path = input("Enter file path: ")
        if not file_path or not os.path.exists(file_path):
            raise Exception("File does not exist.")

        with open(file_path, "rb") as file:
            file_data = file.read()
            self.message = file_data.decode()
            print("Message is read from file.")

    def create_file_signature(self):
        self.read_file()
        self.create_signature()

    def verify_file_signature(self):
        self.read_file()
        self.verify_signature()

    def show_signature(self):
        print("Showing signature.")
        print("Signature: ", self.hex_signature)

    def get_available_features(self):
        available_features = [
            ("Set message", self.set_message),
            ("Set signature", self.set_signature),
            ("Create signature", self.create_signature),
            ("Verify signature", self.verify_signature),
            ("Create file signature", self.create_file_signature),
            ("Verify file signature", self.verify_file_signature),
            ("Show signature", self.show_signature),
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
    service = DSSService()
    while True:
        if not service.show_initial_options():
            break
