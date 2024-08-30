import random

l = [random.randint(0, 100) for n in range(9)]

for i in range(len(l) - 1):
    for j in range(len(l) - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]
