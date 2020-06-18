def r_multiply(a, b):
    if a == 1:
        return b

    return r_multiply(a - 1, b) + b


print(r_multiply(3, 12))
