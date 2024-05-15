def sumOfEncryptedInt(nums) -> int:
    sum = 0
    nums_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
                 "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    for num in nums:
        arr = [*str(num)]
        for i in range(len(arr)):
            arr[i] = nums_dict[arr[i]]

        sum += int(str(max(arr)) * len(arr))
    return sum
