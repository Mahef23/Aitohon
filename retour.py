def demandernom():
    nom =  input("Name : ")
    return nom

def demanderage(nom):
    taona = input(f"{nom}'s Age : ")
    try:
        taonai= int(taona)+1
    except ValueError:
        print("NUmbber!!!!")
    return taona

def afficher(nom, taona):
    print()
    if taona == 17:
        print(f"{nom} , Almost an adult")
    elif taona ==18:
        print(f"{nom} , Congtrats")
    elif taona > 60:
        print(f"{nom} , Oh Mister")
    elif taona > 18:
        print(f"{nom} , You're an adult")
    elif taona < 10 :
        print(f"{nom} , Still Child")
    else:
        print(f"{nom} , Minor")

name = demandernom()
age = demanderage(name)
afficher(name,int(age))

