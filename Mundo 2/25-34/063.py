ter=int(input("termos: "))
t2=1
t1=0
print("{} - {}".format(t1,t2),end="")
cont=3
while cont<=ter:
    t3=t2+t1
    print(" -",t3,end="")
    t1=t2
    t2=t3
    cont+=1
    