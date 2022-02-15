import datetime
a=datetime.datetime.now()
a=int(a.strftime('%Y'))
p=0
for x in range(0,8):
    an=int(input("nasceu em: "))
    if a-an>=21:
        p+=1

print("{} pessoas são maiores de idade".format(p))