import random
def demander_nombre(a,b):
    nombre_int=0
    while nombre_int==0:
        nombre=(input(f"Devinez le chiffre , Il vous reste: {vie} essai(s)"))
        try:
            nombre_int=int(nombre)
        except ValueError:
            print("Erruer veuilllez rentrer un nombre")
        else:
            if min>nombre_int or max<nombre_int:
                print(f"Erreur: Ton chiffre doit être entre {a} et {b}")
                nombre_int=0
    return nombre_int
def chiffre_magique(user,vie,min,max,reponse):
    while user!=reponse and vie>0:
        user= demander_nombre(min,max)
        if(user>reponse):
            print("C'est moins")
            vie=vie-1
        elif(user<reponse):
            print("C'est plus ")
            vie=vie-1
        elif(user==reponse):
            print("C'est Gagné!!!")
    if(vie==0):
        print(f"Vous avez perdu.La bonne reponse etait {reponse}")

user=0
vie=3
min=1
max=10
reponse = random.randint(min,max)
chiffre_magique(user,vie,min,max,reponse)