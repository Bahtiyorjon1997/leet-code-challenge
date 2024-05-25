def longestCommonPrefix(strs) -> str:
    common_pr = ""
    isTrue = True
    if "" in strs:
        return ""
    elif len(strs) == 1:
        return strs[0]
    else:
        for i in strs[0]:
            for j in strs:
                if i not in j:
                    isTrue = False
                    break
                else:
                    common_pr += strs[0][i]
            if not isTrue:
                break
    return common_pr
