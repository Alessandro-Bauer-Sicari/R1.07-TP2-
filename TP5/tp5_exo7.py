import os
import datetime

f1 = input("Fichier 1 : ")
f2 = input("Fichier 2 : ")

if os.path.isfile(f1):
    print("Taille", f1, ":", os.path.getsize(f1))
if os.path.isfile(f2):
    print("Taille", f2, ":", os.path.getsize(f2))

if os.path.isfile(f1) and os.path.isfile(f2):
    t1 = os.path.getmtime(f1)
    t2 = os.path.getmtime(f2)
    if t1 > t2:
        print(f1, "plus récent", datetime.datetime.fromtimestamp(t1))
    else:
        print(f2, "plus récent", datetime.datetime.fromtimestamp(t2))