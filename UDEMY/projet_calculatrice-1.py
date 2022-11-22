#---projet calculatrice---#

#rentrer un premier nombre A
a = input("Entrez un premier nombre: ")
#vérifier que A est un nombre:
while a.isdigit() == False :
        print("Ceci n'est pas un nombre")
        a = input("Entrez un premier nombre: ")
if a.isdigit():
#rentrer un second nombre B
    b = input("Entrez un second nombre: ")
#vérifier que B est un nombre
    while b.isdigit() == False :
        print("Ceci n'est pas un nombre")
        b = input("Entrez un premier nombre: ")
    if b.isdigit() :
    #additionner A & B
        resultat = int(a) + int(b)
    #afficher resultat
        print(f"le résultat de l'addition de {a} et de {b} est: {resultat}")
        


