def s(n):
    n = str(n)
    if len(n[:len(n)]) == 1:
        return int(n[0])
    return int(n[-1]) + s(int(n[:len(n) - 1]))

print(s(input()))
