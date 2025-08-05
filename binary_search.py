def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


numbers = sorted(
    [
        2,
        54,
        67,
        54,
        675,
        67,
        76,
        87,
        12,
        64,
    ]
)

print(numbers)

print(binary_search(numbers, 54))
