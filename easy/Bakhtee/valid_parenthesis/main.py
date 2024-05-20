# data structure used: stack
def valid_parenthesis(string):
    stack = []
    map = {")": "(", "}": "{", "]": "["}
    for char in string:
        if char in map.values():
            stack.append(char)
        elif char in map.keys():
            if not stack or map[char] != stack.pop():
                return False

    return not stack


print(valid_parenthesis('(]'))
