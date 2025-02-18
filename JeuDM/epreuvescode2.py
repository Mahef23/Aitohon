import time
def transform(temps):
    while temps>=60 :
        temps-=60
        global minutes
        minutes+=1
        global secondes 
        secondes= temps
    print(f"{minutes} : {secondes}")
    print()
temps=int(input("Entrer le temps: "))
minutes=0
secondes=0
transform(temps)
if(temps<=60):
    secondes=temps
for i in range (minutes,-1,-1):
    for j in range(secondes,-1,-1):
        time.sleep(0.2)
        print(f"{i} : {j}" , flush=True)

    secondes=59