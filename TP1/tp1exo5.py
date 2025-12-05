
jour = int(input("Entrez le jour du mois : "))
heure = int(input("Entrez l'heure (entre 0 et 23) : "))
minute = int(input("Entrez les minutes (entre 0 et 59) : "))


total_minutes = jour * 24 * 60 + heure * 60 + minute


print("Le nombre de minutes écoulées depuis le début du mois est :", total_minutes)
