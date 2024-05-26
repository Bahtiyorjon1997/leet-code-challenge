def removeElement(nums, val: int) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)
