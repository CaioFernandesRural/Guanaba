import datetime
x = datetime.datetime.now()
an=int(input("Ano nascimento: "))

if an==x.year:
    print("Seu saco há de ser apalpado")
elif x.year>an and int(x.strftime('%Y'))-an-18>0:
    dis=int(x.strftime('%Y'))-an-18
    print("Já passou da hora de ser apalpado em: {} anos".format(dis))
elif int(x.strftime('%Y'))-an-18<=0:
    dis=an-int(x.strftime('%Y'))+18
    print("Ainda faltam {} anos para seu saco ser apalpado.".format(dis))
