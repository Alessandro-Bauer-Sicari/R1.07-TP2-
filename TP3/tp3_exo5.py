debut = int(input("Donnez l’heure de début de la location (un entier) : "))
fin = int(input("Donnez l’heure de fin de la location (un entier) : "))

if debut < 0 or fin < 0 or debut > 24 or fin > 24:
    print("Les heures doivent être comprises entre 0 et 24 ")
elif debut == fin:
    print("réecrivée , en effet  l’heure de fin est identique à l’heure de début.")
elif debut > fin:
    print("réecrivée , en effet le début de la location est après la fin ...")
else:
    tarif1 = 0
    tarif2 = 0

    for i in range(debut, fin):
        if (i >= 0 and i < 7) or (i >= 17 and i < 24):
            tarif1 += 1
        else:
            tarif2 += 1

    print("durée location:")
    if tarif1 > 0:
        print(f"{tarif1} heure(s) au tarif horaire de 1.0 euro")
    if tarif2 > 0:
        print(f"{tarif2} heure(s) au tarif horaire de 2.0 euro")

    total = tarif1 * 1 + tarif2 * 2
    print(f"Le montant total à payer est de {total:.1f} euro.")

