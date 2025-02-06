import turtle

def escalier(taille,marche):
    for i in range(0,marche):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        taille=taille-10
    t.forward(taille)

def carre(taille):
    for i in range (0,4):
        t.forward(taille)
        t.left(90)
t= turtle.Turtle()
#escalier(50,5)
for i in range (0,5):
    carre(20*((-2)**i))
turtle.done()