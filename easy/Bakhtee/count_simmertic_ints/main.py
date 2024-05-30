def isSimmetric(num: int) -> bool:
    isSim = True
    str_num = str(num)
    if len(str_num) <= 1:
        return False
    for i in range(len(str_num) // 2):
        if str_num[i] != str_num[0 - (i + 1)]:
            isSim = False
    return isSim


def countSymmetricIntegers(low: int, high: int) -> int:
    num_count = 0
    for num in range(low, high):
        if isSimmetric(num):
            num_count += 1
    return num_count


print(countSymmetricIntegers(1, 9)
# print(isSimmetric(66))
