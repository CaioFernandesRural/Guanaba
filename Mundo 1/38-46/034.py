sal=float(input("Salario: "))
if sal>1250:
    nsal=sal*0.1+sal
else:
    nsal=sal*0.15+sal
print("{} e o novo salario".format(nsal))