import random

a = [random.randint(0, 1000000) for x in range(100)]
a_s = sorted(a)
m = a_s[-1]

for i in range(1, len(a_s)):
    m = min(m, a_s[i] - a_s[i - 1])

print(m)
