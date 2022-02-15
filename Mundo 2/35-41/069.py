cnov=0
cmai=0
chom=0
c=1
while True:
    print("-----{}ª PESSOA -----".format(c))
    no=input("Nome: ").strip().upper()
    id=int(input("Idade: "))
    sx=input("Sexo? [H/M] ").strip().upper()
    if id>=18:
        cmai+=1
    if sx=="H":
        chom+=1
    if sx=="M" and id<20:
        cnov+=1
    esc=input("Continuar? S/N: ").strip()
    if esc not in "SimSIMsim":
        break
    c+=1

print(f"Temos: {cmai} maiores de idade,{chom} homens e {cnov} novinha(s)")