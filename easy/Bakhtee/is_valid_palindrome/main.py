def isPalindrome(s: str):
    s.lower()
    new_s = ''
    letters = "abcdefghijklmnopqrstuvwxyz"
    nums = '1234567890'
    isPal = True

    for char in s:
        if char.lower() in letters or char in nums:
            new_s += char

    if len(new_s) <= 1:
        return True
    new_s = new_s.lower()

    for i in range(len(new_s)//2):
        if new_s[i] != new_s[0-(i+1)]:
            isPal = False
            break
    return isPal


print(isPalindrome("A man, a plan, a canal: Panama"))
