v=float(input("Velocidade: "))
Lv=int(input("Limite de velocidade: "))
Lvv=(Lv*0.2+Lv)
if v >= Lvv:
    mul=(v-Lvv)*7
    print("Voce foi multado em {} reais".format(mul))
else:
    print("Sem multa.")
