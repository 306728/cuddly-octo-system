o = {}
l = input()

for i in range(len(l)):
    try:
        o[l[i]] += 1
    except KeyError:
        o[l[i]] = 1

s = sorted(o)

print(f"Top 3 letters that occur the most: {s[0], s[1], s[2]}\nTop 3 letters that occur the least: {s[-1], s[-2], s[-3]}")
print(f"{s[0]}{s[1]}{s[2]}{s[-1]}{s[-2]}{s[-3]}")
