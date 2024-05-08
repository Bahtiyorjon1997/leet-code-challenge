
def findRelativeRanks(score):
    score_copy = score.copy()
    score_copy.sort(reverse=True)
    score_dict = {}
    rank_list = []
    for i in range(len(score)):
        score_dict[score_copy[i]] = i+1
    for i in range(len(score)):
        if score_dict[score[i]] == 1:
            rank_list.append('Gold Medal')
        elif score_dict[score[i]] == 2:
            rank_list.append('Silver Medal')
        elif score_dict[score[i]] == 3:
            rank_list.append('Bronze Medal')
        else:
            rank_list.append(score_dict[score[i]])
    return rank_list


print(findRelativeRanks([5, 4, 3, 2, 1]))
