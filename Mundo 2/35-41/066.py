n=0
s=-999
c=-1
while True:
    n=int(input("Número: "))
    s+=n
    c+=1
    if n==999:
        break
print(f"Soma: {s} dos {c} números digitados.")
