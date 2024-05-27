def rotate(nums, k: int) -> None:
    """
        Do not return anything, modify nums in-place instead.
        """
    for i in range(k):
        nums[:] = [nums[-1]] + nums[:-1]
