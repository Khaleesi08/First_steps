#-------------------jeu de rôle-------------------#

from random import randint


# 2 options
options = ["1", "2"]

#nombre de points de vie chacun
mylife = int(50)
yourlife = int(50)

#nombre de potions
potions = 4
yourpotion = 0

#Toutes ces opérations se répètent tant que le joueur et l'ennemi sont en vie
while not (mylife or yourlife) <= 0: 
    #"Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "
    user_input = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2):")

    if not user_input.isdigit() and user_input == options:
        continue

    user_input = int(user_input)

    #Option (1)
    if user_input == 1:
        #points de vie infligés
        myattacts = randint(5, 10)
        yourattacts = randint(5, 15)
        yourstatus = yourlife - myattacts
        mystatus = mylife - yourattacts
        print(f"Vous avez infligé {myattacts} points de dégât à l'ennemi.")
        print(f"L'ennemi vous a infligé {yourattacts} points de dégât.")
        print(f"Il vous reste {mystatus} points de vie.")
        print(f"Il reste {yourstatus} points de vie à l'ennemi.")
        print("-"*40)

    #Option (2)
    elif user_input == 2:
        if potions > 3:

            #points de vie récupérés
            life_retrieved = randint(15, 50)

            print(f"Vous avez récupéré {life_retrieved} points de vie.({potions} restant)")
            print(f"L'ennemi vous a infligé {yourattacts} points de dégât.")
            mylife = (mylife + life_retrieved) - yourattacts
            print(f"Il vous reste {mylife} points de vie.")
            print(f"Il reste {yourstatus} points de vie à l'ennemi.")
            print("-"*40)

            print("Vous passez votre tour")
            print(f"L'ennemi vous a infligé {yourattacts} points de dégât.")
            mylife = mylife - yourattacts
            print(f"Il vous reste {mylife} points de vie.")
            print(f"Il reste {yourstatus} points de vie à l'ennemi.")
            print("-"*40)
        else:
            user_input = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2):")
       
        continue

    mylife -= yourattacts
    yourlife -= myattacts
    potions -= 1

print("Game Over.")