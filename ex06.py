import random

nombre_aleatoire = random.randint(1, 100)

while True:
    nombre_choisi = int(input("Devinez un nombre entre 1 et 100 : "))
    if nombre_choisi < nombre_aleatoire:
        print("Trop petit ! Essayez encore.")
    elif nombre_choisi > nombre_aleatoire:
        print("Trop grand ! Essayez encore.")
    else:
        print("Félicitations ! le nombre est :", nombre_aleatoire)
        break