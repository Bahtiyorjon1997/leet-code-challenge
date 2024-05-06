# Runtime:  51ms  => beats 67,46% of users with python3
# Memory:  16.54 mg => beats 64,67% of users with python3

def isPalindrome(x: int) -> bool:
    str_x = str(x)
    half_len = len(str_x) // 2
    isPol = True
    if len(str_x) == 1:
        return True
    if str_x[-1] == '0' or str_x[0] == "-":
        return False
    for i in range(half_len):
        if str_x[i] != str_x[-(i+1)]:
            isPol = False
    return isPol
