nt=term=1
tot=0
n=int(input("primeiro termo: "))
r=int(input("razão: "))
term=10
while term!=0:
    tot=tot+term
    while nt<=tot:
        t=n+(nt-1)*r
        nt+=1
        print(t)
    term=int(input("quer ver quantos mais termos?: "))
    


