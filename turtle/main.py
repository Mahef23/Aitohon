import turtle

def escalier(taille,marche):
    for i in range(0,marche):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        taille=taille-10
    t.forward(taille)

def carre(taillei,nombre):
    for i in range (1,nombre):
        taille=(taillei*i)
        t.forward(taille)
        t.left(90)
t= turtle.Turtle()
#escalier(50,5)
for i in range (0,5):
    carre(20,10)
turtle.done()