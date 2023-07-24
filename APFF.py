class BigInt:
    def __init__(self, num_str="0"):
        self.digits = [int(digit) for digit in num_str]

    def __str__(self):
        return "".join(str(digit) for digit in self.digits)

    def __add__(self, other):
        return self.addition(self, other)

    def __sub__(self, other):
        return self.subtraction(self, other)

    def __mul__(self, other):
        return self.multiplication(self, other)

    def __truediv__(self, other):
        return self.division(self, other)

    def addition(self, num1, num2):
        result = []
        carry = 0
        i, j = len(num1.digits) - 1, len(num2.digits) - 1

        while i >= 0 or j >= 0 or carry:
            d1 = num1.digits[i] if i >= 0 else 0
            d2 = num2.digits[j] if j >= 0 else 0
            total = d1 + d2 + carry
            carry, digit = divmod(total, 10)
            result.insert(0, digit)
            i, j = i - 1, j - 1

        return BigInt("".join(str(digit) for digit in result))

    def subtraction(self, num1, num2):
        if num1 < num2:
            return "-" + self.subtraction(num2, num1).__str__()

        result = []
        borrow = 0
        i, j = len(num1.digits) - 1, len(num2.digits) - 1

        while i >= 0:
            d1 = num1.digits[i]
            d2 = num2.digits[j] if j >= 0 else 0
            diff = d1 - d2 - borrow

            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0

            result.insert(0, diff)
            i, j = i - 1, j - 1

        # Remove leading zeros
        while result[0] == 0 and len(result) > 1:
            result.pop(0)

        return BigInt("".join(str(digit) for digit in result))

    def multiplication(self, num1, num2):
        result = BigInt("0")

        for i, digit in enumerate(reversed(num2.digits)):
            temp = []
            carry = 0

            for j in reversed(num1.digits):
                prod = digit * j + carry
                carry, val = divmod(prod, 10)
                temp.insert(0, val)

            if carry:
                temp.insert(0, carry)

            for _ in range(i):
                temp.append(0)

            result = result.addition(result, BigInt("".join(str(digit) for digit in temp)))

        return result

    def division(self, num1, num2):
        if int(num2) == 0:
            raise ValueError("Division by zero is not allowed.")

        dividend = int(num1)
        divisor = int(num2)

        quotient = dividend // divisor
        remainder = dividend % divisor

        return BigInt(str(quotient)), BigInt(str(remainder))


def main():
    try:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        operator = input("Enter the operator (+, -, *, /): ")

        big_num1 = BigInt(num1)
        big_num2 = BigInt(num2)

        if operator == '+':
            result = big_num1 + big_num2
        elif operator == '-':
            result = big_num1 - big_num2
        elif operator == '*':
            result = big_num1 * big_num2
        elif operator == '/':
            quotient, remainder = big_num1 / big_num2
            print("Quotient:", quotient)
            print("Remainder:", remainder)
            return
        else:
            print("Invalid operator.")
            return

        print("Result:", result)

    except ValueError as e:
        print("Invalid input:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
