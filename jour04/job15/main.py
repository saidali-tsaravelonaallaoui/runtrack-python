nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

def arrondir_nombre(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

def trier_liste(lst):
    for _ in lst:
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

nombres_arrondis = [arrondir_nombre(n) for n in nombres]
nombres_tries = trier_liste(nombres_arrondis)

print(nombres_tries)
