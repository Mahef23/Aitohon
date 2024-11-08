nom = input("Name : ")
math= input("Note math: ")
svt=input("Note Science: ")
physic = input("Note Physique: ")

moyenne = (int(math) + int(svt) + int(physic))/3


if moyenne< 60:
    print(f"{nom}, you Failed . MARK= {moyenne}")
elif moyenne>=60 and moyenne<70:
    print(f"{nom}, you Passed . MARK= {moyenne}")
else:
    print(f"{nom},Good . MARK= {moyenne}")

