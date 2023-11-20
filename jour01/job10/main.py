montant_initial = 7000
taux_de_rendement_annuel = 10

gain_annuel_1 = montant_initial * (taux_de_rendement_annuel / 100)
print("Le gain annuel est de :", gain_annuel_1, "euros pour un taux de rendement annuel de", taux_de_rendement_annuel, "%")

montant_initial += 5000
taux_de_rendement_annuel += 2

gain_annuel_2 = montant_initial * (taux_de_rendement_annuel / 100)
print("Le gain annuel de la deuxième session est de :", gain_annuel_2, "euros pour un taux de rendement annuel de", taux_de_rendement_annuel, "%")

montant_initial -= montant_initial * 0.10
taux_de_rendement_annuel -= 1

montant_final = montant_initial
gain_final = montant_final * (taux_de_rendement_annuel / 100)

print("Le montant final de l'investissement est de", montant_final, "euros et un gain total de", gain_final, "euros.")
