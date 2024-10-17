
nom = input("Quel est votre nom? ")
age = input("Quel est votre age? ")
profession = input("Quel est votre profession? ")
try:
    agei= int(age)+1
except:
    print("Error")
else:
    print(f"Vous vous appelez {nom} et vous avez {age} ans")
    print(f"Donc l'année prochaine vous avez {agei}")

print(f"Et vous travaillez dans le domaine {profession}")