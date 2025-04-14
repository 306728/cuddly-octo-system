import time

l = []
for i in range(int(input("Number of elements: "))):
    l.append(input())

s = time.time()
j = len(l)
while j > 1:
    k = j
    i = 0
    while k > 1:
        if l[i] > l[i + 1]:
            l[i], l[i + 1] = l[i + 1], l[i]
        i += 1
        k -= 1
        print(k)
        print(l)
    j -= 1
    print(f"J: {j}")
e = time.time()

print(l)
print(f"Sorting duration: {round((e - s) / 1000, 10)} ms")
