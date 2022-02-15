import os
s=m=esc=0
n1=int(input("Digite um número inteiro   : "))
n2=int(input("Digite outro número inteiro: "))

while esc!=5:
    print("[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair")
    esc=int(input("Sua escolha: "))
    if esc==1:
        s=n1+n2
        print("{} + {} = {}.".format(n1,n2,s))
        os.system('pause')
    elif esc==2:
        m=n1*n2
        print("{} x {} = {}.".format(n1,n2,m))
        os.system('pause')
    elif esc==3:
        if n1>n2:
            print("{} > {}".format(n1,n2))
            os.system('pause')
        elif n2>n1:
            print("{} < {}".format(n2,n1))
            os.system('pause')
    elif esc==4:
        n1=int(input("Digite um número inteiro   : "))
        n2=int(input("Digite outro número inteiro: "))
        os.system('pause')
    else:
        print("Incompetente.")
        os.system('pause')

print("Fim")
os.system('pause')