def majorityElement(nums) -> int:
    nums_set = list(set(nums))
    max_num = 0
    majority_element = nums[0]
    for num in nums_set:
        if nums.count(num) > max_num:
            max_num = nums.count(num)
            majority_element = num
    return majority_element


# print(majorityElement([2, 3, 2]))
print(majorityElement([3, 2, 3]))
