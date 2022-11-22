#générer un nombre aléatoire compris entre 0 et 100
import random

nombre_mystere = random.randint(0, 100)
print(nombre_mystere)

#Le joueur dispose de 5 essais
i = 5

while i > 0:
    print(f"Il vous reste {i} essai(s)")

    #choix de l'utilisateur
    user_input = input("Devine le nombre : ")

    if not user_input.isdigit():
        print("Veuillez rentrer une valeur numérique.")

        continue

    user_input = int(user_input)

    #indiquer au joueur si le nombre qu'il a entré est plus petit ou plus grand que le nombre mystère.
    if user_input > nombre_mystere:
        print(f"le nombre entré est plus grand que le nombre mystère.")
    elif user_input < nombre_mystere:
        print(f"le nombre entré est plus petit que le nombre mystère.")
    #Si le nombre entré par l'utilisateur est égal au nombre mystère, alors le joueur gagne la partie.
    #nombre mystère trouvé, indiquer combien d'essais ont été nécessaire pour gagner.
    elif user_input == nombre_mystere:
        print(f"Trouvé! Le nombre mystère était bien {nombre_mystere}.\nVous avez trouvé le nombre en {6 - i} essai(s)")
        
        break   
    i -= 1
#Si le nombre mystère non trouvé avec les 5 essais disponibles, partie perdue.
if i == 0:
    print("Dommage! Le nombre mystère n'a pas été trouvé.")

        