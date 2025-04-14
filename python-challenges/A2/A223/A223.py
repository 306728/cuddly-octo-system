for i in range(101, 1001):
    s = 0
    for j in range(len(str(i))):
        s += int(str(i)[j])
    if i % s == 0:
        print(i)
