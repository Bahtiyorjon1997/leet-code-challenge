def singleNumber(nums) -> int:
    for n in set(list(nums)):
        if nums.count(n) == 1:
            return n
            break
