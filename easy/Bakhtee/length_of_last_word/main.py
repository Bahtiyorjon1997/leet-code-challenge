def lengthOfLastWord(s: str) -> int:
    return len(s.strip().split(" ")[-1])
