def sortColors(nums) -> None:
    """
        Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 1:
        return nums

    for i in range(nums):
        if nums[i] == min(nums):
