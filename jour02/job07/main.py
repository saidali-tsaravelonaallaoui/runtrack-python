ma_chaine = "abcdefghijklmnopqrstuvwxyz" * 10
longueur_chaine = len(ma_chaine)

for i in range(1, longueur_chaine + 1):
    print(ma_chaine[:i])