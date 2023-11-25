L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
def nbr(L):
    c = 0
    for tri in L:
        c += 1
    for n in range(1, c):
        b = L[n]
        x = n - 1
        while x >= 0 and L[x] > b:
            L[x + 1] = L[x]
            x = x - 1
        L[x + 1] = b
    print(L)
nbr(L)
