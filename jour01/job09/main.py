nom = "Ordinateur Portable"
prix_unitaire = 800
quantité_en_stock = 16

print("Produit :", nom)
print("Prix :", prix_unitaire)
print("Quantité :", quantité_en_stock)

ajout = int(input("Entrez la quantité de produits à ajouter au stock :"))
quantité_en_stock += ajout

prix_unitaire *= 1.10

prix_unitaire_entier = int(prix_unitaire)

print("Produit :", nom)
print("Prix :", prix_unitaire_entier)
print("Quantité :", quantité_en_stock)
