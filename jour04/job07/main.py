L = [1, 2, 3, 4, 5]

nbr = 0
for i in range(len(L)):
    if L[i] % 3 == 0:
        nbr += i
        
print(nbr)