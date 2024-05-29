def addDigits(num: int) -> int:
    if num < 10:
        return num
    else:
        num_list = [*str(num)]
        num = sum([int(n) for n in num_list])
        return addDigits(num)


print(addDigits(38))
