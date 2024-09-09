def NAND(a, b):
    if a == 1 and b == 1:
        return 0
    else:
        return 1

def AND(a, b):
    return NAND(NAND(a, b), NAND(a, b))

def XOR(a, b):
    return NAND(NAND(NAND(a, b), b), NAND(NAND(a, b), a))

print(XOR(1, 1))
