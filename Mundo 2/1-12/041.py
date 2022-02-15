import datetime
i=int(input("ano nascimento: "))
x = datetime.datetime.now()
id=int(x.strftime('%Y'))-i

if id<9:
    cat="MIRIM"
elif id>=9 and id<14:
    cat="INFANTIL"
elif id>=14 and id<19:
    cat="JÚNIOR"
elif id==19:
    cat="SÊNIOR"
else:
    cat=("MASTER")
print("Sua categoria : ",cat)