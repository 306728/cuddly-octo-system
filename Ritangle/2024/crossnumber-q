f = open("primes.txt")

primes = []
palindromicprimes = []
cubes = [27, 64]

for line in f:
    line = str(line).strip()
    if len(line) == 2:
        primes.append(int(line))
    if len(line) == 3 and line[0] == line[2]:
        palindromicprimes.append(int(line))

def solve():
    for a in palindromicprimes:
        ac1 = a
        for b in cubes:
            dn4 = b
            for i in range(10):
                if int(f"{str(ac1)[1]}{i}") in primes:
                    dn2 = int(f"{str(ac1)[1]}{i}")
                    ac3 = int(f"{str(dn2)[1]}{str(dn4)[0]}")
                    for j in range(10):
                        for k in range(10):
                            ac5 = int(f"{j}{k}{str(dn4)[1]}")
                            if ac5 == sum(int(x) for x in str(ac5)) ** 2 + int(str(ac3)[::-1]):
                                for l in range(10):
                                    dn1 = int(f"{str(ac1)[0]}{l}{str(ac5)[0]}")
                                    if dn1 == ac1 - sum(int(x) for x in str(dn1)):
                                        return ac1, dn4, dn2, ac3, ac5, dn1

print(solve())
