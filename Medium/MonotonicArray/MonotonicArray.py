def solution1(nums):
    inc = True
    dec = True
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            dec = False
        if nums[i] < nums[i-1]:
            inc = False
    return inc or dec