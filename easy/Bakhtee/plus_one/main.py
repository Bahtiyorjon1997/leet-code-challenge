
def plusOne(digits):
    return [int(digit) for digit in str(int("".join(str(digit) for digit in digits))+1)]


print(plusOne([9, 9]))
