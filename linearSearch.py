
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


numbers = [3, 5, 7, 10]

print(linear_search(numbers, 10))
