new_list = [1, 2, 3, 4]
result = new_list[0]

if 1 in new_list:
    print(True)


for n in new_list:
    if n == 1:
        print(True)
        break


numbers = []
print(len(numbers))

(numbers.append(2))

print(numbers)

import sys

# nums = []
# for i in range(10):
#     nums.append(i)
#     print(i, sys.getsizeof(nums))


numeros = []

numeros.extend([4, 5, 6, 7])

print(numeros)
