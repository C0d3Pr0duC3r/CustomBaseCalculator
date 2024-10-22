import string

base26 = list(range(10))+list(string.ascii_lowercase)
print(base26)
class CustomBase:
    def __init__(self, base: int, symbols=base26):
        # base defines the numbersystem
        # symbols is to be used if base is bigger than 10
        self.base = base
        self.symbols = symbols

    def show(self):
        # prints the number to the screen
        pass

    def convert_to_dec(self):
        # converts the n-based number into a decimal
        pass

    def convert_to_base(self):
        # converts the number to the n-based
        pass


