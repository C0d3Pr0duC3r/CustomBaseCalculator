import string
base26 = list(map(str, range(10))) + list(string.ascii_uppercase)
class CustomBase:
    def __init__(self, base: int, symbols=base26):
        # base defines the numbersystem
        # symbols is to be used if base is bigger than 10
        self.base = base
        self.symbols = symbols

    def show(self):
        # prints the number to the screen
        pass

    def convert_to_dec(self, base_number):

        base_number = str(base_number)
        # converts the n-based number into a decimal
        decimal_value = 0
        power = 0  # Zählt die Potenz der Basis

        # Gehe durch die Ziffern von rechts nach links (umgekehrte Reihenfolge)
        for digit in reversed(base_number):
            decimal_value += int(digit) * (self.base ** power)
            power += 1

        return decimal_value

    def convert_to_base(self, dec):
        """
        dec // self.base = new_dec
        dec % self.base = last_digit
        ...
        new_dec // self.base = 0
        new_dec % self.base = first_digit
        """

        if dec == 0:
            return "0"

        digits = []
        while dec > 0:

            digits.append(self.symbols[dec % self.base])
            dec //= self.base


        return ''.join(reversed(digits))





#8/2 4/2 2/2 1/2
binary = CustomBase(2)

hex = CustomBase(16)

print(binary.convert_to_base(127))

print(binary.convert_to_dec(1010100))

print(hex.convert_to_base(1232))