# def removeElement(nums, val: int) -> int:
#     if val in nums:
#         for num in nums:
#             if num == val:
#                 nums.remove(num)
#         return len(nums)
#     print(nums)
#     return len(nums)


# print(removeElement([2, 3, 2, 2, 4], 2))

nums = [2, 3, 2, 2]
for num in nums:
    if num == 2:
        nums.remove(num)
print(nums)
