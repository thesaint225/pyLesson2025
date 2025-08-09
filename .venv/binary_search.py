def binary_search(my_List, target):
    first = 0
    last = len(my_List) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if my_List[midpoint] == target:
            return midpoint
        elif my_List[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print("target found at index:", index)
    else:
        print("target not found in list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)
