def singleNumber(nums) -> int:
    for n in nums:
        if nums.count(n) == 1:
            return n
