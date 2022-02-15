n1=int(input("Numero: "))
n2=int(input("Numero: "))
n3=int(input("Numero: "))

if n1>n2 and n1>n3:
    print("{} e o maior".format(n1))
elif n2>n1 and n2>n3:
    print("{} e o maior".format(n2))
else:
    print("{} e o maior".format(n3))

if n1<n2 and n1<n3:
    print("{} e o menor".format(n1))
elif n2<n1 and n2<n3:
    print("{} e o menor".format(n2))
else:
    print("{} e o menor".format(n3))