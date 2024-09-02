v = ['a', 'e', 'i', 'o', 'u']
w = input()
l = []

i = 0

while i < len(w):
    if w[i] in v or w[i] == " ":
        l.append(w[i])
    else:
        c = 1
        n = 1
        while i + n < len(w) and w[i + n].isalpha() and  w[i + n] not in v:
            c += 1
            n += 1
        for j in range(c):
            l.append(w[i + j])
        l.append("o")
        for j in range(c):
            l.append(w[i + j])
        i += c - 1
    i += 1

print(l)
        
print("".join(l))
