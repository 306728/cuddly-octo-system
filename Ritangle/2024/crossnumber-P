f = open("squares.txt")
g = open("primes.txt")
h = open("triangle.txt")


squares = [int(line.strip()) for line in f if len(line.strip()) == 3]
primes = [int(line.strip()) for line in g if len(line.strip()) == 2]
triangle = [int(line.strip()) for line in h if len(line.strip()) == 2]


def solve():
    for a in squares:
        ac1 = a
        for b in primes:
            ac3 = b[::-1]
            for i in range(10):
                if (int(i) + int(ac3[0])) ** (1/2) // 1 == (int(i) + int(ac3[0])) ** (1/2):
                    dn2 = int(i) + int(ac3[0])
                    for j in range(10):
                        if int(f"{ac3[1]}{j}") in triangle:
                            dn4 = int(f"{ac3[1]}{j}")
                            k = 0
                            while dn4 * primes[0] < 1000 and str(dn4 * primes[0])[0] == str(ac1)[0]:
                                dn1 = int(dn4 * primes[0])
                                k += 1
                                
