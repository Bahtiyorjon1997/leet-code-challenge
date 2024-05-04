'''
Runtime: 332ms.   Beats 40.42% of python users on leetcode
Memory: 17.37mb.  Beats 84.26% of the python users on leetcode
'''


def twoSum(self, nums, target):
    if len(nums) == 2:
        return [0, 1]
    else:
        for i in range(len(nums)-1):
            if target-nums[i] in nums[i+1:]:
                return [i, i+1+nums[i+1:].index(target-nums[i])]
                break
