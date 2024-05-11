# Runtime:46ms beats 60%
# Memory: 16.52MB beats 70%

def romanToInt(s: str) -> int:
    num_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    sum = 0
    if len(s) == 1:
        return num_dict[s[0]]
    for i in range(len(s)):
        if i+1 < len(s):
            if num_dict[s[i]] >= num_dict[s[i+1]]:
                sum += num_dict[s[i]]
            else:
                sum -= num_dict[s[i]]
    sum += num_dict[s[-1]]
    return sum
