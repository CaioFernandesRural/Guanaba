import random
npc=random.randint(1,2)
vit=res=0
while True:
    ejog=input("Par ou Impar: ").strip().upper()
    njog=int(input("Número: "))
    res=npc+njog
    if ejog=="PAR" and res%2!=0:
        break
    elif ejog=="PAR" and res%2==0:
        print("Ganhou miserávi.")
        vit+=1
    elif ejog=="IMPAR" and res%2!=0:
        print("Ganhou miserávi.")
        vit+=1
    elif ejog=="IMPAR" and res%2==0:
        break
    
print(f"Perdeu Lixo, ganhou {vit}")