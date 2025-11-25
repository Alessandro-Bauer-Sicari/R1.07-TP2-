
etudiant1 = {
    "firstname": "titi",
    "name": "toto",
    "promo": 2022,
    "group": 202
}
print(f"votre nom est '{etudiant1['name']}', prénom est '{etudiant1['firstname']}', "
      f"vous faites partie de la promo '{etudiant1['promo']}' et votre groupe est '{etudiant1['group']}'")

print("\nLes clés du dictionnaire sont :")
for cle in etudiant1.keys():
    print("-", cle)

print("\nLes valeurs du dictionnaire sont :")
for valeur in etudiant1.values():
    print("-", valeur)

print("\nLes tuplets du dictionnaire sont :")
for couple in etudiant1.items():
    print("-", couple)

etudiant2 = {
    "firstname": "tata",
    "name": "tutu",
    "promo": 2022,
    "group": 102
}

binome = {
    "poste1": etudiant1,
    "poste2": etudiant2
}

print("\nLes étudiants formants le binôme sont :")
for identifiant, etu in binome.items():
    print(f"- L'étudiant {etu['name']} {etu['firstname']} du groupe {etu['group']}")
