def pair_impair(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            print(f"{nombre} est un nombre entier positif et pair.")
        else:
            print(f"{nombre} est un nombre entier positif et impair.")
    else:
        print("Le nombre n'est pas un chiffre entier positif.")

pair_impair(6)
pair_impair(15)
pair_impair(-3)
pair_impair(5.5)