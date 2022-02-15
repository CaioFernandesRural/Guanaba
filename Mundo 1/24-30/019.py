import random
from re import L
n1,n2,n3,n4=input("Digite 4 nomes: ").split()
lis=[n1,n2,n3,n4]
random.shuffle(lis)
print("ordem de apresentação: ",lis)