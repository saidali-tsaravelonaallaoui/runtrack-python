nombre_marches = 10
hauteur_marche = 20

def calculate_distance(marches, hauteur_marche):

    distance_aller_retour = 2 * marches * hauteur_marche / 100

    distance_journaliere = 5 * distance_aller_retour

    distance_hebdomadaire = 7 * distance_journaliere

    return distance_hebdomadaire

distance_totale = calculate_distance(nombre_marches, hauteur_marche)

print(f'Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_totale:.2f} m par semaine.')
