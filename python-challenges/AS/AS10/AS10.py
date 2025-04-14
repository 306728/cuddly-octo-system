l = []
v = ["a", "e", "i", "o", "u"]
s = ["ab", "cd", "pq", "xy"]
n = 0
nl = {}

for i in range(int(input())):
    l.append(input())

for i in range(len(l)):
    c = 0
    r = 0
    if "ab" not in l[i] and "cd" not in l[i] and "pq" not in l[i] and "xy" not in l[i]:
        for j in range(len(l[i])):
            if l[i][j] in v:
                c += 1
            if j < len(l[i]) - 1 and l[i][j] == l[i][j + 1]:
                r += 1
        if c >= 3 and r >= 1:
            nl[l[i]] = "nice"
        else:
            nl[l[i]] = "naughty"
    else:
        nl[l[i]] = "naughty"

print(nl)
