import math

def f(x, y, n):
    l = []
    for i in range(n):
        a = int(math.factorial(n)/(math.factorial(i) * math.factorial(n - i)))
        if a == 1:
            if i == 0:
                l.append(f"({x})^{n} + ")
            else:
                l.append(f"({x})^{n - i}({y})^{i} + ")
        else:
            if i == 0:
                l.append(f"{a}({x})^{n} + ")
            else:
                l.append(f"{a}({x})^{n - i}({y})^{i} + ")
    l.append(f"({y})^{n}")
    return "".join(l)

print(f(input(), input(), int(input()))
