reponse = 45
vie=4
for i in range (0,vie):
    user=int(input(f"Vous avez {vie} pour devniez le chiffre: "))
    if(user<reponse):
        print("C'est plus")
    elif(user>reponse):
        print("C'est moins")
    elif(user==reponse):
        print("C'est Gagné")
        break
    vie=vie-1

if vie==0:
    print("Vous avez perdu")