L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

long = len(L)

c = 1
for i in range (0, long) :
     if 25 <= L[i] <= 90 :
          c = c*L[i]
print ("Produit des valeurs entre 25 et 90 :", c)