from random import randint
tup=(randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))
men=mai=tup[0]
print(tup)

if tup[1]>tup[0] and tup[1]>tup[2] and tup[1]>tup[3] and tup[1]>tup[4]:
    mai=tup[1]
elif tup[2]>tup[0] and tup[2]>tup[1] and tup[2]>tup[3] and tup[2]>tup[4]:
    mai=tup[2]
elif tup[3]>tup[0] and tup[3]>tup[2] and tup[3]>tup[1] and tup[3]>tup[4]:
    mai=tup[3]
elif tup[4]>tup[0] and tup[4]>tup[2] and tup[4]>tup[3] and tup[4]>tup[1]:
    mai=tup[4]

if tup[1]<tup[0] and tup[1]<tup[2] and tup[1]<tup[3] and tup[1]<tup[4]:
    men=tup[1]
elif tup[2]<tup[0] and tup[2]<tup[1] and tup[2]<tup[3] and tup[2]<tup[4]:
    men=tup[2]
elif tup[3]<tup[0] and tup[3]<tup[2] and tup[3]<tup[1] and tup[3]<tup[4]:
    men=tup[3]
elif tup[4]<tup[0] and tup[4]<tup[2] and tup[4]<tup[3] and tup[4]<tup[1]:
    men=tup[4]

print(f"{mai} é o maior e {men} é o menor")