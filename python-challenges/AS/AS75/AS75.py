def bcd(n):
    l = []
    s = ""
    for _ in range(len(n)):
        l.append([])
    for i in range(len(n)):
        d = int(n[i])
        if d >= 8:
            l[i].append(str(d // 8))
            d -= 8
        else:
            l[i].append("0")
        if d >= 4:
            l[i].append(str(d // 4))
            d -= 4
        else:
            l[i].append("0")
        if d >= 2:
            l[i].append(str(d // 2))
            d -= 2
        else:
            l[i].append("0")
        if d % 2 == 1:
            l[i].append("1")
        else:
            l.append("0")
    for i in range(len(l)):
        s += ("".join(l[i]) + " ")
    return s

print(bcd(input()))
