def canConstruct(ransomNote: str, magazine: str) -> bool:
    isTrue = True
    for c in ransomNote:
        if ransomNote.count(c) > magazine.count(c):
            isTrue = False
    return isTrue
