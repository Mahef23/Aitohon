vera= 0
toakaL= 2
def matsaka(litre):
    global toakaL
    toakaL +=litre
    print("Matsaka")

if vera == 0 :
    vera +=2
    toakaL -=2
    if toakaL == 0:
        while  toakaL < 15:
            matsaka(2)
    else:
        print("Mitohy ny revy")