mai=men=0

lis=[0]
for x in range(1,6):
    pes=int(input("peso {}: ".format(x)))
    if x==1:
        mai=men=pes
    else:
        if pes>mai:
            mai=pes
        elif pes<men:
            men=pes

print("{} maior, {} menor".format(mai,men))