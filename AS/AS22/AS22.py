def dot_product(u, v):
    p = 0
    for i in range(len(u)):
        p += u[i] * v[i]
    return p
