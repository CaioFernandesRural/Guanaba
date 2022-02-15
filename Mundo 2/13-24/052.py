n=int(input("numero: "))
t=0
for x in range(1,n+1):
    if n%x==0:
        print('\033[32m',end="")
        t+=1
    else:
        print("\033[31m",end="")
    print("{} ".format(x),end="")
   
print("\n\033[m{} foi divisível {} vezes\n".format(n,t))
if t>2:
    print("não é primo")
else:
    print(" é primo")