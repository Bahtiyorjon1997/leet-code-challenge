"""
Runtime: 47ms Beats 5.95% of users with Python3
Memory: 16.48MB Beats 90.49% of users with Python3
"""


def numberOfSpecialChars(word: str):
    unique_char_count = len(set(list(word.lower())))
    lst_of_char = list(set(list(word.lower())))
    counter = 0
    if len(word) == unique_char_count:
        return 0
    for i in range(unique_char_count):
        if lst_of_char[i] in word and lst_of_char[i].upper() in word:
            counter += 1
    return counter
