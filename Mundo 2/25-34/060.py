n=int(input("Digite inteiro: "))
nf=n
fat=1
while nf>0:
    print(nf,end='')
    print(" x "if nf>1 else " = ", end="")
    fat=fat*nf
    nf-=1
print("{}".format(fat),end="")