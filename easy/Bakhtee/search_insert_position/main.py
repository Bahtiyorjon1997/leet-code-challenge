def searchInsert(nums, target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)


print(searchInsert([1, 2, 3, 4], 5))
