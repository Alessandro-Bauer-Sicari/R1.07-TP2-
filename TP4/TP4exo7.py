
binome = ("login1", "login2")


print(f"L’étudiant {binome[0]} est en binome avec l’étudiant {binome[1]}")


nouveau_login = input("Entrez le nouveau login pour le second étudiant : ")
try:
    binome[1] = nouveau_login   # ⚠️ ceci va provoquer une erreur !
except TypeError:
    print("Erreur : les tuplets sont immuables, on ne peut pas modifier un élément.")


try:
    del binome[1]
except TypeError:
    print("Erreur : les tuplets sont immuables, on ne peut pas supprimer un élément.")

trinome = binome + ("login3",)
print(f"Trinome formé : {trinome}")
