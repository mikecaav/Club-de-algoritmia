def solution1(arr):
    res = 0
    for indx in range(1, len(arr) - 1):
        if arr[indx - 1] < arr[indx] > arr[indx + 1]:
            l = r = indx
            while l > 0 and arr[l] > arr[l - 1]:
                l -= 1
            while r + 1 < len(arr) and arr[r] > arr[r + 1]:
                r += 1
            res = max(res, r - l + 1)
    return res
