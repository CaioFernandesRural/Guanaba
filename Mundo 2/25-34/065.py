n=dig=s=1
mai=men=0
cont="sim"
while cont in "simyes":
    n=int(input("Digite um número: "))
    s=s+n
    dig+=1
    if n>mai:
        men=mai=n
    elif n<men:
        men=n
    cont=input("Continuar: ").strip().lower()
    
        
m=(s)/(dig)
print("a soma dos seus {} numeros digitados é: {}\n maior: {} menor: {}".format(dig,s,mai,men))