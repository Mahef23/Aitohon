import time
choix=int(input("Vous voulez: \n 1- Ouef a la coque \n 2- Oeuf mollets \n 3-Oeuf Dur "))
if(choix==1):
    print("Durée : 3 minutes") 
    temps=180
elif(choix==2):
    print("Durée : 6 minutes") 
    temps=360
elif(choix==3):
    print("Durée : 9 minutes") 
    temps=540

minute= temps//60
seconde= temps-(minute*60)

for i in range (minute,-1,-1):
    for j in range (seconde,-1,-10):
        print(f"{i:02d}:{j:02d} ", end="")
        for k in range (10,-1,-1):
            time.sleep(0.2)
            print("." , end="" , flush=True)
        print()
    seconde=50
print("Cuisson Terminé")