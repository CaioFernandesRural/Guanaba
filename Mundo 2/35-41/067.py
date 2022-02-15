n=fat=1

while True:
    n=int(input("Número: "))
    print("")
    if n<0:
        break
    for x in range(1,11):
        print(f"{n} x {fat} = {fat*n}")
        fat+=1
      
print("Fim\n")