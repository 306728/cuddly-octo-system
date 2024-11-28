f = open("squares.txt")
g = open("primes.txt")
h = open("triangles.txt")


squares = [int(line.strip()) for line in f if len(line.strip()) == 3]
primes = [int(line.strip()) for line in g if len(line.strip()) == 2]
triangle = [int(line.strip()) for line in h if len(line.strip()) == 2]


def solve():
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                if (i + j + k) in primes:
                    ac5 = int(f"{i}{j}{k}")
                    for a in squares:
                        if len(ac5 - a) == 2 and int(str(ac5 - a)[1]) == int(str(ac5)[2]):
                            dn4 = ac5 - a
                            ac3 = dn4 - sum([int(x) for x in str(dn4)])
                            for l in range(1, 10):
                                for m in range(1, 10):
                                    

print(solve())
