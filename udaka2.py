age = 0
while age == 0:
    age_str=input("Entrer un age: ")
    try:
        age = int(age_str)
    except ValueError:
        print("Erreur de Varaible")

print("Vous avez "+str(age)+" ans")
print("L\'année prochaine vous aurez "+str(age+1)+" ans")