def tri(n):
    if n == 1 or n == 2:
        return 0
    elif n == 3 or n == 4: 
        return 1
    return tri(n - 1) + tri(n - 2) + tri(n - 3)

def tetra(n):
    if n <= 3:
        return 0
    elif n == 4 or n == 5:
        return 1
    return tetra(n - 1) + tetra(n - 2) + tetra(n - 3) + tetra(n - 4)
