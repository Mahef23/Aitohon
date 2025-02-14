def poucecm(valeur):
    valeur*=2.54
    return valeur 

def cmpouce(valeur):
    valeur*=0.394
    return valeur

kit=True
choix= float(input("Entrer : \n 1 si vous voulez une conversion de pouce en cm et \n 2 si vous voulez une conversion de cm en pouce \n Votre Choix: "))
while kit==True:
    print()
    chiffre= float(input("Entrer la valeur que vous voulez convertir: "))
    if choix == 1:
        print(f"{poucecm(chiffre)} cm ")
    else:
        print(f"{cmpouce(chiffre)} pouce")
    print("Vous voulez arrêtez?")
    qit=input("0-Oui ou N-Non --->")
    if qit == "O":
        kit=False
    kit=True