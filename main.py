from features.LinearCongruentialGenerator import linear_congruential_generator as lcg
from features.MD5 import md5_service as md5
from features.RC5 import rc5_service as rc5
from features.RSA import rsa_service as rsa_encryption
from features.DSS import dss_service as dss

import os

available_features = [
    ("Linear Congruential Generator", lcg.entry_point),
    ("MD5", md5.entry_point),
    ("RC5-CBC-Pad", rc5.entry_point),
    ("RSA", rsa_encryption.entry_point),
    ("DSS", dss.entry_point),
]

def show_initial_options():
    print("Main menu")
    while True:
        print("Choose the option:")
        for i in range(len(available_features)):
            print(f"{i + 1}. {available_features[i][0]}")
        print("0. Exit")

        try:
            option = int(input("Option: "))
            if option == 0:
                print("Goodbye!")
                return False

            os.system("clear")
            print(f"Chosen option: {available_features[option - 1][0]}")
            available_features[option - 1][1]()
            print("after call")
        except Exception as e:
            continue

def main():
    while True:
        if not show_initial_options():
            break


if __name__ == "__main__":
    main()