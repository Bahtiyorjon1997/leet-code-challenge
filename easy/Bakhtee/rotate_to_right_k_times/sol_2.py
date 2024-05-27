def rotate(nums, k: int) -> None:
    """
        Do not return anything, modify nums in-place instead.
        """
    for i in range(k):
        temp = nums.pop()
        nums.insert(0, temp)
