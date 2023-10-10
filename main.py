from features.LinearCongruentialGenerator import linear_congruential_generator as lcg

available_features = [
    ("Linear Congruential Generator", lcg.entry_point),
]

def show_initial_options():
    print("Main menu")
    while True:
        print("Choose the option:")
        for i in range(len(available_features)):
            print(f"{i + 1}. {available_features[i][0]}")
            print("0. Exit")

        option = int(input("Option: "))
        if option == 0:
            print("Goodbye!")
            return False

        available_features[option - 1][1]()


def main():
    while True:
        if not show_initial_options():
            break


if __name__ == "__main__":
    main()