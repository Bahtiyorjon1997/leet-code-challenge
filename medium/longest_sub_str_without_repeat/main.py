def lengthOfLongestSubstring(s: str) -> int:
    sub_strs = []
    sub_s = s[0]
    for i in range(len(s)):
        sub_s = s[i]
        for j in range(i+1, len(s)):
            if s[i] != s[j] and s[j] not in sub_s:
                sub_s += s[j]
            else:
                break
        if sub_s:
            sub_strs.append(sub_s)
        sub_s = ""

    return len(max(sub_strs, key=len))


# print(lengthOfLongestSubstring('abcabcbb'))
lengthOfLongestSubstring("pwwkew")
# lengthOfLongestSubstring('bbbb')
# print(len(max(['a', 'bsd', 'ffff'])))
