an=int(input("Ano: "))

if an%4==0 or an%100!=0 or an%400==0:
    print("si bissexto")    
else:
    print("no bissexto.")