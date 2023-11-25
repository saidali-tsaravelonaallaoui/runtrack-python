liste_notes = [37, 45, 82, 91, 64]

def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note >= 40 and note % 5 >= 3:
            note_arrondie = note + (5 - note % 5)
        else:
            note_arrondie = note
        notes_arrondies.append(note_arrondie)
    return notes_arrondies

notes_arrondies = arrondir_notes(liste_notes)

print(liste_notes)
print(notes_arrondies)
