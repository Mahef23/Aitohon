import random
def question():
    point=0
    for i in range (4):
        print(f"Qestion {i+1} /4")
        reponse=False
        calc= random.randint(1,4)
        a=random.randint(1,10)
        b=random.randint(1,10)
        if(calc==1):
            fanontanina=float(input(f"Calculer {a} + {b} ="))
            vrai=a+b
            if(fanontanina==vrai):
                reponse=True
        elif(calc==2):
            fanontanina=float(input(f"Calculer {a} - {b}="))
            vrai=a-b
            if(fanontanina==vrai):
                reponse=True
        elif(calc==3):
            fanontanina=float(input(f"Calculer {a} * {b} ="))
            vrai=a*b
            if(fanontanina==vrai):
                reponse=True
        elif(calc==4):
            if(a>b):
                vrai=a/b
                fanontanina=float(input(f"Calculer {a} / {b}="))
            else:
                vrai=b/a
                fanontanina=float(input(f"Calculer {b} / {a} ="))
            if(fanontanina==vrai):
                reponse=True
        
        if (reponse==False):
            print(f"Perdu , la reponse était {vrai}")
        else:
            print("Gagne")
            point+=1
    print(f"Vous avez une note de {point}/4")



question()