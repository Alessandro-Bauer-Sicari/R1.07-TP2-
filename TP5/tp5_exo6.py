T = input("Chaîne : ")
taille = 0
for c in T:
    taille += 1

v = 0
for c in T.lower():
    if c in "aeiouy":
        v += 1

print("Taille :", taille)
print("Pourcentage voyelles :", v*100/taille)

cpt = 0
prem = -1
for i in range(taille-4):
    if T[i:i+5] == "wagon":
        cpt += 1
        if prem == -1:
            prem = i

print("Première occurrence :", prem)
print("Nombre d'occurrences :", cpt)