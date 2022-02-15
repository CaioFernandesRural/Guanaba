import random
n=random.randrange(0,11)
adv=int(input("Chuta o numero: "))
palp=0
while adv!=n:
    print("errou.")
    adv=int(input("Chuta o numero, horroroso: "))
    palp+=1
print("acertou depois de {} tentativas também né?".format(palp))
