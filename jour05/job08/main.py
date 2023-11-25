ma_liste = [42, 17, 8, 32, 91, 54, 23, 5]

def my_sort(lst):
    n = len(lst)
    coups = 0
    trie = False

    while not trie:
        trie = True  
        for i in range(n-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                trie = False
                coups += 1

    print(f"Nombre total de coups nécessaires pour trier la liste : {coups}")
    print(f"La liste triée est : {lst}")

    return lst

resultat = my_sort(ma_liste)