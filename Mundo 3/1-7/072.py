ext=("Zero","Um","Dois","Tres","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez",
"Onze","Doze","Treze","Catorze","Quinze","Dezesseis","Dezesete","Dezoito","Dezenove","Vinte")

while True:
    n=int(input("Divite um número de 0 a 20: "))
    if n>=0 and n<=20:
        print(f"{n} por extenso é: {ext[n]}")
        break