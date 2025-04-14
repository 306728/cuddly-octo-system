def reverse_string(s):
    l = list(s)
    for i in range(len(s) - 1, -1, -1):
        l[len(s) - i - 1] = s[i]
    return "".join(l)

print(reverse_string(input()))
