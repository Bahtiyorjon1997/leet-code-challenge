from collections import defaultdict


def maximumNumberOfStringPairs(words) -> int:
    dict_ = defaultdict(int)
    for i, word in enumerate(words):
        dict_[word[::-1]] = i
    pairs = 0
    extra = []
    for i, element in enumerate(words):
        if element in dict_ and dict_[element] != i and element not in extra:
            pairs += 1
            extra.append(element[::-1])
        else:
            continue
    return pairs
