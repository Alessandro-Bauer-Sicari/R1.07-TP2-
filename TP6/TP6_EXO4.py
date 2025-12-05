import random

def generer(nbr, vmin, vmax):
    table = []
    for i in range(nbr):
        table.append(random.randint(vmin, vmax))
    return table

def combienInferieur(table, vseuil):
    compteur = 0
    for val in table:
        if val < vseuil:
            compteur += 1
    return compteur


nbr = int(input("Combien de valeurs voulez-vous générer ? "))
vmin = int(input("Valeur minimale : "))
vmax = int(input("Valeur maximale : "))


reponse = input("Vous voulez préciser le seuil ? (Oui/O ou Non/N) : ")

if reponse.lower() in ["oui", "o"]:
    vseuil = int(input("Précisez le seuil : "))
else:
    vseuil = 30

print(f"\nGénérer {nbr} nombres entiers entre {vmin} et {vmax}")
tab = generer(nbr, vmin, vmax)
tab.sort()
print("Tableau généré trié :", tab)

total = combienInferieur(tab, vseuil)
print(f"Il y en a {total} inférieurs à {vseuil}")
