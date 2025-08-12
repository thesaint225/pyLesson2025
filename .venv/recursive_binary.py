def recursive_binary_search(my_list, target):
    if len(my_list) == 0:
        return False
    else:
        midPoint = (len(my_list)) // 2
        if my_list[midPoint] == target:
            return True
        else:
            if my_list[midPoint] < target:
                return recursive_binary_search(my_list[midPoint + 1 :], target)
            else:
                return recursive_binary_search(my_list[:midPoint], target)


def verify(result):
    print("Target found", result)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)

verify(result)
