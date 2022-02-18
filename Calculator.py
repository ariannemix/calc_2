from Converter import BinaryConverter

converter = BinaryConverter()


class Calculator:

    def __init__(self, x=None, y=None):
        self.open = True
        self.x = x
        self.y = y

    def binary(self):
        binary = input("Enter a binary number to convert: ")
        converter = BinaryConverter(binary=binary)
        try:
            print(f"\n{binary} = {converter.bin_to_dec()}\n")
        except:
            print("\nPlease enter a valid input.")

    def decimal(self):
        integer = int(input("Enter a decimal number to convert: "))
        converter = BinaryConverter(integer=integer)
        try:
            print(f"\n{integer} = {converter.dec_to_bin()}\n")
        except:
            print("\nPlease enter a valid input.")

    def add(self):
        result = ''
        max_length = max(len(self.x), len(self.y))

        self.x = self.x.zfill(max_length)
        self.y = self.y.zfill(max_length)

        carry = 0

        for i in range(max_length - 1, -1, -1):
            if self.x[i] == '0' and self.y[i] == '0' and carry == 0:
                result = '0' + result
            elif self.x[i] == '0' and self.y[i] == '0' and carry == 1:
                result = '1' + result
                carry = 0
            elif self.x[i] != self.y[i] and carry == 0:
                result = '1' + result
            elif self.x[i] != self.y[i] and carry == 1:
                result = '0' + result
            elif self.x[i] == '1' and self.y[i] == '1' and carry == 0:
                result = '0' + result
                carry = 1
            elif self.x[i] == '1' and self.y[i] == '1' and carry == 1:
                result = '1' + result

        if carry > 0:
            result = '1' + result

        return converter.remove_zeros(result)

    def subtract(self):
        result = ''

        max_length = max(len(self.x), len(self.y))

        self.x = self.x.zfill(max_length)
        self.y = self.y.zfill(max_length)
        borrow = 0
        converter_x = BinaryConverter(binary=self.x)
        converter_y = BinaryConverter(binary=self.y)
        if converter_x.bin_to_dec() < converter_y.bin_to_dec():
            print("ERROR: This difference results in a negative number.")

        for i in range(max_length - 1, -1, -1):
            if self.x[i] == '0' and self.y[i] == '0' and borrow == 0:
                result = '0' + result
            elif self.x[i] == '1' and self.y[i] == '0' and borrow == 0:
                result = '1' + result
            elif self.x[i] == '1' and self.y[i] == '1' and borrow == 0:
                result = '0' + result
            elif self.x[i] == '0' and self.y[i] == '1' and borrow == 0:
                result = '1' + result
                borrow += 1
            elif self.x[i] == '0' and self.y[i] == '1' and borrow != 0:
                result = '0' + result
            elif self.x[i] == '1' and self.y[i] == '0' and borrow != 0:
                result = '0' + result
                borrow -= 1
            elif self.x[i] == '1' and self.y[i] == '1' and borrow != 0:
                result = '1' + result
                borrow += 1
            elif self.x[i] == '0' and self.y[i] == '0' and borrow != 0:
                result = '1' + result
        if '1' not in result:
            return '0'
        else:
            return converter.remove_zeros(result)

    def multiply(self):
        result = ''

        max_length = max(len(self.x), len(self.y))

        self.x = self.x.zfill(max_length)
        self.y = self.y.zfill(max_length)

        for i in range(max_length - 1, -1, -1):
            if self.y[i] == '0':
                pass
            if self.y[i] == '1':
                num = self.x + ''.zfill(max_length - 1 - i)
                n = Calculator(num, result)
                result = n.add()

        # result = result.zfill(max_length)
        return result

    def divide(self):
        result = ''
        s = self.x[0]
        for i in range(0, len(self.x)):
            if int(s) < int(self.y):
                result += '0'
                if i == len(self.x)-1:
                    return converter.remove_zeros(result)
                else:
                    n = Calculator(s, '0')
                    s = n.subtract() + self.x[i+1]
            elif int(s) >= int(self.y):
                result += '1'
                if i == len(self.x)-1:
                    return converter.remove_zeros(result)
                else:
                    n = Calculator(s, self.y)
                    s = n.subtract() + self.x[i+1]

    def quit(self):
        print(f"\nGoodbye!")
        self.open = False
