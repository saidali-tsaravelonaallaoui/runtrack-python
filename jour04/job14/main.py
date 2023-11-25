ma_phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

def my_long_word(nvl_longueur, phrase):
    resultat = ''
    longueur_mot = 0
    mot = ''
    dans_mot = False

    for char in phrase:
        if char == ' ':
            if dans_mot:
                if longueur_mot > nvl_longueur:
                    resultat += mot + ' '
                longueur_mot = 0
                dans_mot = False
        else:
            longueur_mot += 1
            mot = char if not dans_mot else mot + char
            dans_mot = True

    if dans_mot and longueur_mot > nvl_longueur:
        resultat += mot

    return resultat

print(my_long_word(3, ma_phrase))