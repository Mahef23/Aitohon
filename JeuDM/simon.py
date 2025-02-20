import time
import random
import os

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def gametime(n):
    jeu=True
    score=0
    while jeu==True:
        n1=random.randint(0,9)
        res=n+str(n1)
        print("Retenez le chiffre:")
        time.sleep(1)
        print(res)
        time.sleep(3)
        clear_screen()
        reponse=input(("Entrer la sequence:"))
        if(reponse==res):
            score+=1
            print(f"Gagnez /// Score: {score}")
            n=n+n1
            jeu=True
        else:
            print(f"Perdu /// La sequence etait {res} /// Votre score = {score}")
            jeu=False
        time.sleep(3)
        clear_screen()
        
chiff= random.randint(10,99)
nombre=str(chiff)
gametime(nombre)