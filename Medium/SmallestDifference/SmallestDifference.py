def solution1(arr):
    results = []
    minimal = float('inf')
    arr.sort()

    for (a, b) in zip(arr, arr[1:]):
        diff = abs(b - a)
        if diff == minimal:
            results.append((a, b))
        elif diff < minimal:
            results = [(a, b)]

    return results
