dis=int(input("Digite a distância em km "))
if dis>200:
    pre=dis*0.45
else:
    pre=dis*0.5
print("Preço: {}".format(pre))