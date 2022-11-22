#------------------liste de courses-----------------#

import sys

LISTE_COURSES = []

#CREER LES OPTIONS

choice = ["1", "2", "3", "4", "5"]
i = ""

# Vérifier que les valeurs entrées sont valides
while not i in choice:
    print("Veuillez entrer une valeur comprise entre 1 et 5.\n")
    
    user_input = input("""Choisissez parmi les 5 options suivantes :" 
            1: Ajouter un élément à la liste de courses
            2: Retirer un élément de la liste de courses
            3: Afficher les éléments de la liste de courses
            4: Vider la liste de courses
            5: Quitter le programme
            Votre choix : """)

    #1. Ajouter un élément à la liste de courses
    if user_input == "1":
        item = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        LISTE_COURSES.append(item)
        print(f"L'élément {item} a bien été ajouté à la liste de courses.")

    #2. Retirer un élément de la liste de courses
    elif user_input == "2":
        item = input("Entrez l'élément à retirer de la liste de courses : ")
        if item in LISTE_COURSES:
            LISTE_COURSES.remove(item)
            print(f"L'élément {item} a bien été retiré de la liste de courses.")
        else:
            print(f"{item} n'existe pas dans la liste de courses.")

    #3. Afficher les éléments de la liste de courses
    elif user_input == "3":
        if LISTE_COURSES:
            for i, item in enumerate(LISTE_COURSES, 1):
                print(f"Voici la liste de courses: {i}.{item}")
        else:
            print(" [] \n La liste de courses est vide.")

    #4. Vider la liste de courses
    elif user_input == "4":
        if LISTE_COURSES:
            LISTE_COURSES.clear()
            print("La liste de courses a été vidée.")
        else:
            print("La liste de courses ne contient aucun élément à supprimer.")

    #5. Quitter le programme
    elif user_input == "5":
        print("A Bientôt !")
        sys.exit()
