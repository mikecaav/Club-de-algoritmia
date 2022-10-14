def solution1(nums):
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postFix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postFix
        postFix *= nums[i]
    return res
