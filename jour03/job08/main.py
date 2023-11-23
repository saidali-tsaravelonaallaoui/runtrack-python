def produits(type, saison):
    if type == "fruits":
        if saison == "hiver":
            print("Orange, mandarine et kiwi")
        elif saison == "ete":
            print("Poire, fraise, cassis")
    elif type == "legume":
        if saison == "hiver":
            print("Carotte, topinambour, endive")
        elif saison == "ete":
            print("Artichaut, aubergine, navet")

produits("fruits", "hiver")
produits("fruits", "ete")
produits("legume", "hiver")
produits("legume", "ete")