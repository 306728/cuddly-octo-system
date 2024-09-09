import random
def sum_and_product(l):
    s = 0
    p = 1
    for i in range(len(l)):
        s += l[i]
        p *= l[i]
    print(f"Sum: {s}\nProduct: {p}")

sum_and_product([random.randint(1, 100) for _ in range(50)])
