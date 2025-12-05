import random

tirage = random.randint(0, 2)

if tirage < 2:
    print("Pile !")
else:
    print("Face !")
