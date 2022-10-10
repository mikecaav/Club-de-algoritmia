def solution1(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def solution2(nums, target):
    complementMap = dict()
    for i in range(len(nums)):
        num_ = nums[i]
        complement = target - num_
        if num_ in complementMap:
            return [complementMap[num_], i]
        complementMap[complement] = i
    return [-1, -1]

