def power(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a*power(a, b-1)


print(power(5, 2))
