vaI=int(input("Valor do Imóvel: "))
sal=float(input("Salário: "))
ans=int(input("Quantos anos: "))

parc=vaI/(ans*12)
if sal<parc+parc*0.3:
    print("Emprestimo Negado.")
else:
    print("Emprestimo Aceito.")