v = ["a", "e", "i", "o", "u"]
c = 0
w = input().lower()

for i in range(len(w)):
    if w[i] in v:
        c += 1

print(c)
