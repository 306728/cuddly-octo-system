def GCD(a, b):
    if a == 1 or b == 1:
        return 1
    elif a == 0 or b == 0:
        return min(a, b) + max(a, b)
    return GCD(max(a, b) - min(a, b), min(a, b))

print(GCD(int(input()), int(input())))
