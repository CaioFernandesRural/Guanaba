import random
n1,n2,n3,n4=input("Digite 4 nomes: ").split()
lis1=[n1,n2,n3,n4]
lis2=lis1-random.choice(lis1)
print(lis2)

