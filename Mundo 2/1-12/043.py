p=float(input("Peso: "))
h=float(input("Altura: "))
imc=p/h**2
if imc<18.5:
    print("Abaixo do peso.")
elif imc>=28.5 and imc<25:
    print("Peso ideal.")
elif imc>=25 and imc<30:
    print("Acima do peso.")
elif imc>=30 and imc<40:
    print("Obeso.")
else:
    print("Obeso mórbido")