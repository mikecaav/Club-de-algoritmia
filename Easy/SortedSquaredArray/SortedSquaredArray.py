def solution1(nums):
    return sorted([value**2 for value in nums])


def solution2(nums):
    res = []
    l, r = 0, len(nums) - 1
    while l <= r:
        if nums[l] ** 2 > nums[r] ** 2:
            res.append(nums[l] ** 2)
            l += 1
        else:
            res.append(nums[r] ** 2)
            r -= 1
    return res[::-1]
