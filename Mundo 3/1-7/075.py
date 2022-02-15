a=int(input("Numero 1-10: "))
b=int(input("Numero 1-10: "))
c=int(input("Numero 1-10: "))
d=int(input("Numero 1-10: "))
par=0
tup=(a,b,c,d)

for x in tup:
    if x%2==0:
        par+=1

print(f"Valor 9 aparece  vezes")
print(f"Valor 3 aparece na {(tup.index(3)+1)} posição")
print(f"{par} Números Pares.")