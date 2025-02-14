import random

def question():
    point=0
    for i in range(0,4):
        a=random.randint(1,10)
        b=random.randint(1,10)
        calcul= random.randint(1,4)
        if(calcul==1):
            operator='+'
            vrai=a+b
        elif(calcul==2):
            operator='-'
            vrai=a-b
        elif(calcul==3):
            operator='*'
            vrai=a*b
        else:
            operator='/'
            vrai=a/b
        
        print(f"Qestion n° {i+1}/4 : ")
        valiny=float(input(f"Calculer {a} {operator} {b} : "))
        if valiny == vrai:
            print("Gagne")
            point+=1
        else :
            print(f"Perdu, la reponse était {vrai}")
        print()
    print(f"Vous avez obtenu {point}/4")

question()