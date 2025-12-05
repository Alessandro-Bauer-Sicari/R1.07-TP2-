L1 = [0] * 3
print("Liste L1 :", L1)
print("Type de L1 :", type(L1))
print("ID de L1 :", id(L1))


for i in range(len(L1)):
    print(f"Élément {i} -> valeur : {L1[i]}, type : {type(L1[i])}, id : {id(L1[i])}")


L1[1] += 1
print("\nAprès modification de L1[1] :")
print("Liste L1 :", L1)
print("Type de L1 :", type(L1))
print("ID de L1 :", id(L1))

for i in range(len(L1)):
    print(f"Élément {i} -> valeur : {L1[i]}, type : {type(L1[i])}, id : {id(L1[i])}")

machaine = "machaine"
print("\nVariable machaine :", machaine)
print("Type de machaine :", type(machaine))
print("ID de machaine :", id(machaine))

for i in range(len(machaine)):
    print(f"Caractère {i} -> valeur : {machaine[i]}, type : {type(machaine[i])}, id : {id(machaine[i])}")
