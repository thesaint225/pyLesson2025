# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1


# numbers = [15, 28, 43, 5, 100]
# print(linear_search(numbers, 43))


# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#         return -1
#     number = [15, 43, 56, 76]
#     print(linear_search(number, 43))


# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#         return -1
#     number = [15, 43, 56, 76]
#     print(linear_search(number, 43))


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


numbers = [3, 5, 7, 10]

print(linear_search(numbers, 10))
