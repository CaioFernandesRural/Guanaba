import emoji
ids=0
maioridh=0
nomvel=""
muie=0

for x in range(1,5):
    print("-----{}ª PESSOA -----".format(x))
    no=input("Nome: ").strip().upper()
    id=int(input("Idade: "))
    sx=input("Sexo? [H/M] ").strip().upper()
    ids+=id
    if x==1 and sx=="H":
        maioridh=id
        nomvel=no
    elif sx=="H" and id>maioridh:
        maioridh=id
        nomvel=no
    if sx=="M" and id<20:
        muie+=1


mid=ids/x
print("Média de idade: {}".format(mid))
print("O macho mais velo é {} com {} anos.".format(nomvel,maioridh))
print(emoji.emojize("Temos {} novinha(s)".format(muie)))
