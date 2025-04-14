a = []

def r(l):
    n_l = []
    for i in range(len(l)):
        if n_l.count(l[i]) == 0:
            n_l.append(l[i])
    return n_l

for i in range(int(input())):
    a.append(input())

print(r(a))
