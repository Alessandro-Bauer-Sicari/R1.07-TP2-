def ajouter_elt(lst=[0, 1, 2], elt=3):
    lst.append(elt)
    print("Contenu de lst :", lst, "id :", id(lst))
    return lst

print("Premier appel ajouter_elt() :")
print(ajouter_elt())


print("\nDeuxième appel ajouter_elt() :")
print(ajouter_elt())

print("\nTroisième appel ajouter_elt() :")
print(ajouter_elt())

def ajouter_carac(ch="abc", elt="d"):
    resultat = ch + elt
    print("Chaîne utilisée :", ch, "id :", id(ch))
    print("Résultat obtenu :", resultat, "id :", id(resultat))
    return resultat

# c) Premier appel
print("\nPremier appel ajouter_carac() :")
print(ajouter_carac())

# d) Répéter l’instruction précédente
print("\nDeuxième appel ajouter_carac() :")
print(ajouter_carac())

print("\nTroisième appel ajouter_carac() :")
print(ajouter_carac())
