import string

base36 = tuple(map(str, range(10))) + tuple(string.ascii_uppercase)

'''IMPORTANT: 36 is the highest possible base at the moment!'''

class CustomBaseNumber:
    def __init__(self, base: int, value, symbols=base36):
        self.base = base
        self.symbols = symbols

        # check, if value is already in self.base (String) of if its a decimal (int)
        if isinstance(value, int):
            self.dec_value = value
            self.base_value = self.convert_to_base(self.dec_value)
        elif isinstance(value, str):
            self.base_value = value
            self.dec_value = self.convert_to_dec(self.base_value)
        else:
            raise ValueError("Value must be an integer (decimal) or string (in base representation)")

    def convert_to_dec(self, base_number):
        base_number = list(str(base_number))
        decimal_value = 0
        power = 0

        for symbol in reversed(base_number):
            digit_value = self.symbols.index(symbol)
            decimal_value += digit_value * (self.base ** power)
            power += 1

        return decimal_value

    def convert_to_base(self, dec_value, let_me_see=False):

        check_value = dec_value  # keep original value, to check at the end
        if dec_value == 0:
            return "0"

        digits = []
        count = 0
        while dec_value != 0:
            count += 1
            # show steps
            if let_me_see:
                see_dec, see_remainder = divmod(dec_value, self.base)
                print(f"{dec_value} // {self.base} = {see_dec} R:{see_remainder}")
            dec_value, remainder = divmod(dec_value, self.base)

            if remainder < 0:
                remainder += abs(self.base)
                dec_value += 1

            digits.append(self.symbols[remainder])
            '''if by accident or on purpose a negative number is put into a positive base calculator
            this will ask the user if the program should be terminated'''
            if count % 1000 == 0:
                print(f"convert to base method ran {count}-times, suspected infinite loop, abort?")
                usr_in = input("(Y/N)>_")
                if usr_in in ["y", "Y", "yes", "j", "J"]:
                    exit()

        number_out = ''.join(reversed(digits))

        # check if number_out actually represents the dec_value
        if check_value == self.convert_to_dec(number_out):
            print(f"Success! {check_value} == {self.convert_to_dec(number_out)}")
        else:
            print(f"malfunction!!! {check_value} != {self.convert_to_dec(number_out)}")

        return number_out


    def show(self):
        return f"{self.base_value} in Base {self.base} (Dezimal: {self.dec_value})"

    # give back decimal value
    def to_decimal(self):
        return self.dec_value


class Calculator:
    def __init__(self, calc_base=None):
        self.calc_base = calc_base

    def add(self, *numbers: int):
        values = [CustomBaseNumber(self.calc_base, number) for number in numbers]

        print(f"adding {[value.show() for value in values]} ...")
        result_value = sum([value.to_decimal() for value in values])
        print(CustomBaseNumber(self.calc_base, result_value).show())
        print("-"*12)


negative_decimal_calculator = Calculator(-10)

negative_trinary_calculator = Calculator(-3)

negative_binary_calculator = Calculator(-2)

binary_calculator = Calculator(2)

negative_binary_calculator.add("11", "11")


