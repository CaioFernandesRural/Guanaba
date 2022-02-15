n=input("Numero (0/9999): ")

if len(n)==4:
    print("Unidade: ",n[4])
    print("Dezena : ",n[2])
    print("Centena: ",n[1])
    print("Milhar : ",n[0])
elif len(n)==3:
    print("Unidade: ",n[0])
    print("Dezena : ",n[1])
    print("Centena: ",n[2])
elif len(n)==2:
    print("Unidade: ",n[0])
    print("Dezena : ",n[1])
elif len(n)==1:
    print("Unidade: ",n[0])
else:
    print("me mama")