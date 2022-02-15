s=0
for x in range(1,7):
    n=int(input("numero: "))
    if n%2==0:
        s+=n
print("soma dos pares: {}".format(s))