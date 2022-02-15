fr=input("palavra: ").strip().upper()
pals=fr.split()
frj="".join(pals)
inv=""
for l in range(len(frj)-1,-1,-1):
    inv+=(frj[l])
if frj==inv:
    print("palíndromo.")
else:
    print("no palindromo")
    
print(frj, inv)