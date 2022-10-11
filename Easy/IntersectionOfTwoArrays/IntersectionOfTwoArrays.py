def solution1(nums1, nums2):
    frequencyNums1 = collections.Counter(nums1)
    frequencyNums2 = collections.Counter(nums2)
    return frequencyNums1 & frequencyNums2

def solution2(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return set1 & set2
