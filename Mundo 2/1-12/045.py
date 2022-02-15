import random; import os;os.system('cls')
list=["pedra","papel","tesoura"]
jo=input("pedra, papel ou tesoura? ")
pc=random.choice(list)
print("\ncomputador escolhe: {}\n".format(pc))

if jo=="pedra" and pc=="papel":
    print("perdeu lixo")
if jo=="pedra" and pc=="tesoura":
    print("ganhou.")
if jo=="pedra" and pc=="pedra":
    print("empate")
if jo=="tesoura" and pc=="papel":
    print("ganhou.")
if jo=="tesoura" and pc=="tesoura":
    print("empate")
if jo=="tesoura" and pc=="pedra":
    print("perdeu lixo")
if jo=="papel" and pc=="papel":
    print("empate")
if jo=="papel" and pc=="tesoura":
    print("perdeu lixo")
if jo=="papel" and pc=="pedra":
    print("ganhou.")