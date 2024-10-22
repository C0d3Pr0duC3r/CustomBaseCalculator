import string

base26 = list(map(str, range(10))) + list(string.ascii_lowercase)

class CustomBase:
    def __init__(self, base: int, symbols=base26):
        # base defines the numbersystem
        # symbols is to be used if base is bigger than 10
        self.base = base
        self.symbols = symbols

    def show(self, number):
        print(f"decimal representation: {self.convert_to_dec(number)}, {self.base}-representation: {number}")

    def convert_to_dec(self, number):
        # Converts the n-based number into decimal
        pass

    def convert_to_base(self, decimal):
        #
        pass


