# step 1:clamp  using if/elif/else
def clamp(num):
    if num < 0:
        return 0
    elif num > 255:
        return 225
    else:
        return num


# step 2:convert to 2-digit uppercase hex


def to_hex2(num):
    h = hex(num)[2:].upper()  # convert to hex remove  "0x" make uppercase
    if len(h) == 1:
        return "0" + h
    return h


# step 3
def rgb(r, g, b):
    r = clamp(r)
    g = clamp(g)
    b = clamp(b)
    return to_hex2(r) + to_hex2(g) + to_hex2(b)


print(rgb(225, 99, 71))
