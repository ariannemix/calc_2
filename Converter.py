import math


class BinaryConverter:

    def __init__(self, binary='', integer=0):
        self.binary = binary
        self.integer = integer

    def bin_to_dec(self):
        code = [128, 64, 32, 16, 8, 4, 2, 1]
        binary_code = []
        answer = 0
        for bit in self.binary:
            binary_code.append(bit)
        for i in range(0, len(binary_code)):
            if int(binary_code[i]) > 0:
                answer += code[i + len(code) - len(binary_code)]
        return answer

    def dec_to_bin(self):
        answer = []
        for i in range(0, 8):
            if i == 0:
                answer.append(str(self.integer % 2))
            else:
                self.integer = math.floor(self.integer/2)
                answer.append(str(self.integer % 2))
        answer.reverse()
        final_answer = self.remove_zeros(''.join(answer))
        return final_answer

    def remove_zeros(self, binary_string):
        count = 0
        for i in range(0, 8):
            if binary_string[i] == '1':
                break
            elif binary_string[i] == '0':
                count += 1
        return binary_string[count:]
