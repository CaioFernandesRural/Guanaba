esc=(input("1=Binário \n2=Octal \n3=hexadecimal \nBase de conversão: "))
n=int(input("Digite o numero a ser convertido: "))
if esc=="1":
    print("{} em binário é: {}".format(n,bin(n)[2:]))
elif esc=="2":
    print("{} em octal é: {}".format(n,oct(n)[2:]))
elif esc=="3":
    print("{} em hexadecimal é: {}".format(n,hex(n)[2:]))
else:
    print("vai tomar no seu cu")