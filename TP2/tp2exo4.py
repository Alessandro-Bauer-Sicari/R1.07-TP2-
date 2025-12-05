BASE=4
fromage=800.0
eau=10
ail=2
pain=400

nbconvives= int(input("entrez le nobre de convives :"))
fromage=fromage * nbconvives / BASE
eau= eau * nbconvives / BASE
ail = ail * nbconvives / BASE
pain = pain * nbconvives / BASE

print(f"Pour faire une fondue fribourgeoise pour {nbconvives} personnes, il vous faut :")
print(f"- {fromage} gr de fromage")
print(f"- {eau} dl d'eau")
print(f"- {ail} gousse(s) d'ail")
print(f"- {pain} gr de pain")
