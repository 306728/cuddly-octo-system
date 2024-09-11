def remove_all(a, b):
    while b.count(a) > 0:
        b = b[:b.find(a)] + b[b.find(a) + len(a):]
    return b

print(remove_all(input(), input()))
