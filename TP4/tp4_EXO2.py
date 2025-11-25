nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0;
tot = 0.0
notes = []
for i in range(nombreEtudiants):
    note = float(input(f"note de l'étudiant {i + 1}:"))
    while note < 0 or note >20:
        note = float(input(f"note de l'étudiant {i + 1}:"))
    notes.append(note)
    tot += note
moyenne = round(tot/ nombreEtudiants,2)
print(f"Moyenne de classe : {moyenne}")
print("numero de l'étudiant | note | ecart à la moyenne")
for i in range(nombreEtudiants):
    ecart=round(notes[i]-moyenne,2)
    print (f"{i} | {notes[i]} | {ecart}")




