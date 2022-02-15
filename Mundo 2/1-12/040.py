n1,n2,n3=input("3 Notas: ").split()
m=(float(n1)+float(n2)+float(n3))/3

if m>=7:
    a=("Aprovado.")
elif m<7 and m>=5:
    a=("Em Recuperação.")
else:
    a=("Reprovado.")
print("Você Está",a)
