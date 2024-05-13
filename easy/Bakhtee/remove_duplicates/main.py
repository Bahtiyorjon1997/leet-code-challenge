def removeDuplicates(self, nums) -> int:
    unique_nums = []
    for i in range(len(nums)):
        if nums[i] in unique_nums:
            nums[i] = None
        else:
            unique_nums.append(nums[i])
    nums[:] = unique_nums
    return len(unique_nums)
