import unicodedata
import string

def nettoyer_texte(texte):
    # Mettre en minuscules
    texte = texte.lower()
    # Supprimer les espaces et ponctuations
    texte = ''.join(ch for ch in texte if ch.isalnum())
    return texte

def supprimer_accents(texte):

    texte = unicodedata.normalize('NFD', texte)

    texte = ''.join(ch for ch in texte if unicodedata.category(ch) != 'Mn')
    return texte

def est_palindrome(texte):

    texte_nettoye = nettoyer_texte(supprimer_accents(texte))

    return texte_nettoye == texte_nettoye[::-1]

phrase = input("Entrez un mot ou une phrase : ")

if est_palindrome(phrase):
    print("C'est un palindrome ")
else:
    print("Ce n'est pas un palindrome ")
