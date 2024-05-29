def longestCommonPrefix(strs) -> str:
    common_pr = ""
    min_str = strs[0]
    isTrue = True
    for i in strs:
        if len(i) < len(min_str):
            min_str = i
    for i in range(len(min_str)):
        for j in strs:
            if min_str[i] != j[i]:
                isTrue = False
        if isTrue:
            common_pr += min_str[i]
        else:
            break
    return common_pr


longestCommonPrefix(["flower", "flow", "flight"])
