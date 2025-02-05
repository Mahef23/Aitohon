a = int (input("Capacity A"))
b = int (input("Capacity B"))
ai = int (input("Initial Capacity A"))
bi = int (input("Initial Capacity B"))
af = int (input("Final Capacity A"))
bf = int (input("Final Capacity A"))

print("List of operations: ")
print("1 : Remplissage A")
print("2 : Remplissage B")
print("3 : Vidange A")
print("4 : Vidange B")
print("5 : A vers B ")
print("6 : B vers A")
while((ai!=af or bi!=bf)):
    op= int(input("Opeatrion:"))
    if(op==1):
        ai=a
    elif(op==2):
        bi=b
    elif(op==3):
        ai=0
    elif(op==4):
        bi=0
    elif(op==5):
        if(ai>(b-bi)):
            ai=ai-(b-bi)
            bi=b
        elif(ai<=(b-bi)):
            bi=bi+ai
            ai=0
    elif(op==6):
        if(bi>(a-ai)):
            bi=bi-(a-ai)
            ai=a
        elif(bi<=(a-ai)):
            ai=ai+bi
            bi=0
    print(ai,bi)