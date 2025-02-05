def entrerage():
    age_local = 0
    while age_local == 0:
        age_str=input("Entrer un age: ")
        try:
            age_local = int(age_str)
        except ValueError:
            print("Erreur de Varaible") 
    return age_local

age=entrerage()
print("Vous avez "+str(age)+" ans")
print("L\'année prochaine vous aurez "+str(age+1)+" ans")