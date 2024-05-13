def findWords(words):
    keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    words_list = []
    isInFirstRow = True
    isInSndRow = True
    isInThirdRow = True

    for word in words:
        for char in word.lower():
            if char not in keyboard[0]:
                isInFirstRow = False
                break
            else:
                isInFirstRow = True

        for char in word.lower():
            if char not in keyboard[1]:
                isInSndRow = False
                break
            else:
                isInSndRow = True

        for char in word.lower():
            if char not in keyboard[2]:
                isInThirdRow = False
                break
            else:
                isInThirdRow = True
        if isInFirstRow or isInSndRow or isInThirdRow:
            words_list.append(word)
    return words_list


print(findWords(["Hello", "Alaska", "Dad", "Peace"]))
