def maskify(s):
    # if the input string is 4 or fewer characters,return it directly
    if len(s) <= 4:
        return s
    # otherwise , mask all but the last 4 charcters
    visible_part = s[-4:]  # last 4 characters
    masked_part = "#" * (len(s) - 4)  # create "#"for the rest
    return masked_part + visible_part  # combine and return


print(maskify("123456789"))
