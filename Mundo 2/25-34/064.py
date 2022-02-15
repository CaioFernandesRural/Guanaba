n=dig=s=0
while n!=999:
    n=int(input("Digite um número que não seja 999: "))
    s=s+n
    dig+=1
print("a soma dos seus {} numeros digitados é: {}".format(dig-1,s-999))