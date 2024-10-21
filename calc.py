def mark(res):
    if res<=60 : 
        print("Fail")
    elif  res>60 and res<=70:
        print("Pass")
    else: 
        print("Excellent")
    return res

def average(point):
    isa = point *5
    return isa


print(average(mark(60)))