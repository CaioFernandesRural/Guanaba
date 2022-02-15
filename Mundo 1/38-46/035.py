l1=int(input("Lado1: "))
l2=int(input("Lado2: "))
l3=int(input("Lado3: "))

if l1+l2>l3 or l3+l2>l1 or l1+l3>l2:
    print("condição de existência cumprida")
else:
    print("condição de existência não cumprida")