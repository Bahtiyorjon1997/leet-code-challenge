def mergeArrs(nums1, m, nums2, n):
    nums1 = nums1[:-3] + nums2
    nums1.sort()
    return nums1


print(mergeArrs([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
