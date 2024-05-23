def majorityElement(nums) -> int:
    nums_set = list(set(nums))
    max_num = 0
    for num in nums_set:
        if nums.count(num) > max_num:
            print(num, "worked")
            max_num = num
    return max_num


# print(majorityElement([2, 3, 2]))
print(majorityElement([3, 2, 3]))
