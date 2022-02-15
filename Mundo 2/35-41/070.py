tot=mmil=pb=cont=0
nb=''
while True:
    nom=input("Nome do produto: ")
    p=float(input("Preço: "))
    tot+=p
    cont+=1
    if cont==1 or p<pb:
        pb=p
        nb=nom
    if p>1000:
        mmil+=1
    esc=input("Continuar? (S/N): ").strip().upper()
    if esc not in "SIM":
        break
print(f"Gasto total: {tot}\nProdutos mais de mil: {mmil}\nProduto mais barato: {nb}, custando: {pb}")

