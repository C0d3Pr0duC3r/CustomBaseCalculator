import string

base36 = tuple(map(str, range(10))) + tuple(string.ascii_uppercase)

'''IMPORTANT: 36 is the highest possible base at the moment!'''


# TODO negative base numbers need to work

class CustomBase:
    def __init__(self, base: int, symbols=base36):
        # base defines the numbersystem
        # symbols is to be used if base is bigger than 10
        self.base = base
        self.symbols = symbols

    def convert_to_dec(self, base_number):
        # Konvertiere base_number in eine Liste von Zeichen
        base_number = list(str(base_number))
        decimal_value = 0
        power = 0  # Zählt die Potenz der Basis

        # Iteriere durch die Ziffern von rechts nach links (umgekehrte Reihenfolge)
        for symbol in reversed(base_number):
            # Hole den Index des Symbols in der `symbols`-Liste
            digit_value = self.symbols.index(symbol)

            # Berechne den Stellenwert und addiere ihn zum Ergebnis
            decimal_value += digit_value * (self.base ** power)

            # Erhöhe die Potenz für die nächste Stelle
            power += 1

        return decimal_value

    def convert_to_base(self, dec_value, let_me_see=True):
        """
        dec // self.base = new_dec
        dec % self.base = last_digit
        ...
        new_dec // self.base = 0
        new_dec % self.base = first_digit
        """
        # keep a copy of dec_value to check later
        dec = dec_value

        if dec == 0:
            return "0"

        digits = []
        if self.base != 0:
            while dec != 0:
                if let_me_see:
                    print(f"dec= {dec}")
                    print(f"dec // base => {dec} // {self.base} = {dec // self.base}")
                    print(f"dec % base => {dec} % {self.base} = {dec % self.base}")
                    print(f"==> {dec // self.base}, R: {dec % self.base}")
                    print("-" * 12)

                digits.append(self.symbols[dec % self.base])
                dec //= self.base

                number = ''.join(reversed(digits))

        elif self.base == 0:
            print("base is 0 -> not defined")

        if self.convert_to_dec(number) == dec_value:
            return number

        else:
            print("number conversion went wrong")


class Number:
    def __init__(self, base, dec_value):
        self.base = CustomBase(base)
        self.dec_value = dec_value
        self.base_value = self.base.convert_to_base(self.dec_value)

    def show(self):
        return f"decimal: {self.dec_value}; {self.base.base} -base representation: {self.base_value}"


class Calculator:
    def __init__(self, calc_base=None):
        self.calc_base = calc_base

    """def add(self, *numbers):
        values = [number.dec_value for number in numbers]
        print(f"adding {[number.base.convert_to_base(number.dec_value) for number in numbers]}, decimal representation {values} ...")
        result_value = sum(values)
        Number(numbers[0].base.base, result_value).show()"""

    def add(self, *dec_values: int):
        print(f"adding {[Number(self.calc_base, val).base_value for val in dec_values]} ...")

        result_value = sum(dec_values)
        print(Number(self.calc_base, result_value).show())


trinary_calculator = Calculator(3)

hex_calculator = Calculator(16)

negative_binary = Calculator(-2)

binary = Calculator(2)

binary.add(10)

# trinary_calculator.add(12)


# negative_binary.add(2)
