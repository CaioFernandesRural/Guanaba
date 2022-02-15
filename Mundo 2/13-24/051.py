n=int(input("primeiro termo: "))
r=int(input("razão: "))
dec=n+(10-1)*r

for x in range(n,dec+r,r):
    print(x)
