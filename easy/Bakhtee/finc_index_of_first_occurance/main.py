def strStr(self, haystack: str, needle: str) -> int:
    if needle in haystack:
        return len(haystack.split(needle)[0])
    return -1
