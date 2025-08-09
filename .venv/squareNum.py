def square_digits(num):
    num_str = str(num)
    result = ""
    for digit in num_str:
        squared = int(digit) ** 2
        result += str(squared)

    return int(result)


print(square_digits(4543))
