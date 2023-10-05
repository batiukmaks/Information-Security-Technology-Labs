import csv


class LinearCongruentialGenerator:
    def __init__(self):
        self.a = 0
        self.c = 0
        self.m = 0
        self.x0 = 0
        self.last_sequence = []
        self.last_period = 0

        self.output_filepath = "results.txt"
        self.input_filepath = "example-input.csv"

        print("Welcome to Linear Congruential Generator")
        print("Default parameters are:")
        print(f"a = {self.a}")
        print(f"c = {self.c}")
        print(f"m = {self.m}")
        print(f"x0 = {self.x0}")
        print("Change them using the menu below")

    def print_parameters(self):
        print("Current parameters are:")
        print(f"a = {self.a}")
        print(f"c = {self.c}")
        print(f"m = {self.m}")
        print(f"x0 = {self.x0}")

    def update_params_from_terminal(self):
        print("Updating parameters from terminal")
        while True:
            print("Enter parameters")
            try:
                a = int(input("a (integer): "))
                c = int(input("c (integer): "))
                m = int(input("m (integer): "))
                x0 = int(input("x0 (integer): "))
                break
            except ValueError:
                print("Invalid input. Try again.")

        self.a = a
        self.c = c
        self.m = m
        self.x0 = x0

        self.print_parameters()

    import csv
    def update_params_from_csv_file(self):
        print("Updating parameters from csv file")
        while True:
            print(f"Enter path to csv file with parameters or press Enter to use default file {self.input_filepath}")
            filepath = input("Path: ")
            if not filepath:
                filepath = self.input_filepath

            print(f"Reading parameters from {filepath}")
            try:
                with open(filepath, "r") as file:
                    reader = csv.DictReader(file)

                    # Read first and only row
                    for row in reader:
                        self.a = int(row["a"])
                        self.c = int(row["c"])
                        self.m = int(row["m"])
                        self.x0 = int(row["x0"])
                        break
                break
            except Exception as err:
                print(f"Error while reading parameters from the file: {err}")
        self.print_parameters()


    def print_results(self):
        print("Results:")
        print("Sequence: ", self.last_sequence)
        print("Period: ", self.last_period)


    def generate_value(self, x):
        return (self.a * x + self.c) % self.m

    def generate_sequence(self):
        print("Generating sequence")
        while True:
            try:
                length = int(input("Enter length of sequence: "))
                break
            except ValueError:
                print("Invalid input. Try again.")

        self.last_sequence = []
        curr_x = self.x0
        for i in range(length):
            self.last_sequence.append(curr_x)
            curr_x = self.generate_value(curr_x)

        self.last_period = self.get_period()



    def get_period(self):
        period = None
        for i in range(len(self.last_sequence)):
            if self.last_sequence[i] == self.last_sequence[0] and i != 0:
                period = i
                break
        if not period:
            period = len(self.last_sequence)

        self.last_period = period
        return period

    def save_to_file(self):
        print(f"Enter new path to save results or press Enter to save to {self.output_filepath}")
        new_path = input("Path: ")
        if new_path:
            self.output_filepath = new_path

        try:
            with open(self.output_filepath, "w") as file:
                file.write("Sequence: " + str(self.last_sequence) + "\n")
                file.write("Period: " + str(self.last_period) + "\n")
        except Exception as err:
            print(f"Error while saving results to the file: {err}")

        print(f"Results saved to {self.output_filepath}")

    def get_available_features(self):
        available_features = [
            ("Update parameters from terminal", self.update_params_from_terminal),
            ("Update parameters from csv file", self.update_params_from_csv_file),
            ("Generate sequence", self.generate_sequence),
            ("Save results to file", self.save_to_file),
            ("Print results", self.print_results),
        ]
        return available_features

    def show_initial_options(self):
        available_features = self.get_available_features()
        while True:
            print("Choose the option:")
            for i in range(len(available_features)):
                print(f"{i + 1}. {available_features[i][0]}")
            print("0. Back to main menu")

            try:
                option = int(input("Option: "))
                if option == 0:
                    return False

                available_features[option - 1][1]()
                input("Press Enter to continue...")
            except:
                continue

def entry_point():
    lcg = LinearCongruentialGenerator()
    while True:
        if not lcg.show_initial_options():
            return True




# if __name__ == "__main__":
#     length = int(input("Enter length of sequence: "))
#
#     sequence = generate_sequence(a, c, m, x0, length)
#     period = get_period(sequence)
#     print("Sequence: ", sequence)
#     print("Period: ", period)
#
#     # Save results to file
#     with open("results.txt", "w") as file:
#         file.write("Sequence: " + str(sequence) + "\n")
#         file.write("Period: " + str(period) + "\n")


# Every feature is another module
# .exe file | sh
