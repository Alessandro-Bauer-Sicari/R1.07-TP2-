heures = int(input("Entrez le nombre d'heures travaillées : "))
salaire_horaire = float(input("Entrez le salaire horaire (€) : "))

salaire = 0

if heures <= 160:
    salaire = heures * salaire_horaire
elif heures <= 200:
    salaire = (160 * salaire_horaire) \
              + (heures - 160) * (salaire_horaire * 1.25)
else:
    salaire = (160 * salaire_horaire) \
              + (40 * salaire_horaire * 1.25) \
              + (heures - 200) * (salaire_horaire * 1.50)

print(f"Le salaire total est de {salaire:.2f} €")
