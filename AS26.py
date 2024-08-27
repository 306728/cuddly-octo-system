f = open("file.txt", "r")
L = f.readlines()

s = 0
n = 0

for l in L:
    for i in range(len(l.split())):
        print(l.split()[i])
        s += len(l.split()[i])
        n += 1

print(round(s / n, 2))