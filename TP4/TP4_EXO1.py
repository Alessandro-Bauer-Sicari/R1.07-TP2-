nombre=float(input("donner un nombre dont vous chercher la table :"))

table=[]

for i in range (10):
    resultat = round(nombre * i , 2)
    table.append(resultat)
for i in range(10):
    print(f"{nombre} * {i} = {table[i]}")