f = open("squares.txt")
g = open("primes.txt")
h = open("triangles.txt")

squares = [int(line.strip()) for line in f if len(line.strip()) == 3]
primes = [int(line.strip()) for line in g if len(line.strip()) == 2]
triangle = [int(line.strip()) for line in h if len(line.strip()) == 2]

def solve():
    for a in squares:
        if int(str(a)[1]) != 0:
            ac1 = str(a)
            for b in primes:
                if 1 <= int(str(b)[1]) <= 4:
                    ac3 = str(b)[::-1]
                    if (int(ac1[1]) + int(ac3[0])) ** (1/2) // 1 == (int(ac1[1]) + int(ac3[0])) ** (1/2):
                        dn2 = int(f"{ac1[1]}{ac3[0]}")
                        for i in range(10):
                            if int(f"{ac3[1]}{i}") in triangle:
                                dn4 = int(f"{ac3[1]}{i}")
                                for c in primes:
                                    if str(dn4 * c)[0] == str(ac1)[0] and len(str(dn4 * c)) == 3 and int(str(dn4 * c)[2]) != 0:
                                        dn1 = int(dn4 * c)
                                        for j in range(1, 10):
                                            if (sum(int(x) for x in str(ac1)) + sum(int(x) for x in str(ac3)) + int(str(dn4)[1]) + sum(int(x) for x in str(dn1)[1:]) + j) % 9 == 0:
                                                ac5 = int(f"{str(dn1)[2]}{j}{str(dn4)[1]}")
                                                return ac1, ac3, dn2, dn4, dn1, ac5

print(solve())
