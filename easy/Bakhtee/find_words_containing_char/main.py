# Runtime:  50ms  => beats 96.40% of users with python3
# Memory:  16.56 mg => beats 78.25% of users with python3


def findWordsContaining(words, x: str):
    words_with_x = []
    for i in range(len(words)):
        if x in words[i]:
            words_with_x.append(i)
    return words_with_x
