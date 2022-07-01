fmobiles=open("mobile.txt")
all_mobiles=[]
for line in fmobiles:
    mobile=line.rstrip("\n").split(",")
    all_mobiles.append(mobile)
print(all_mobiles)

costlymob=max(all_mobiles,key=lambda mob :int(mob[2]))
print(costlymob)

fiveG=[mob for mob in all_mobiles if mob[3]=="5g"]
print(fiveG)