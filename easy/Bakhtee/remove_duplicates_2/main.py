def removeDuplicates(nums) -> int:
    nums_unique = list(set(nums))
    for num in nums_unique:
        while nums.count(num) > 2:
            nums.remove(num)

    return len(nums)
