p=float(input("Preço: "))
fp=input("cartão ou dinheiro? ")

if fp=="dinheiro":
    pt=p-p*0.1
elif fp=="cartão":
    cart=input("à vista ou parcelado? ")
    if cart=="à vista":
        pt=p-p*0.05
    elif cart=="parcelado":
        parc=int(input("Quantas parcelas? 20% de juros a partir de 3. "))
        if parc==2:
            pt=p
        else:
            pt=p+p*0.2

print("Preço total: ",pt)    