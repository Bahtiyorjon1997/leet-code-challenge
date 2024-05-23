
def mySqrt(x: int) -> int:
    sqrt = 0
    if x <= 1:
        return x

    for i in range((x//2)+1):
        if i*i <= x:
            sqrt = i
        else:
            break
    return sqrt
