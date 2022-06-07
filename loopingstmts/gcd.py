num1 = 15
num2 = 60
num3=45
hcf = 1

# limit=min(num1,num2,num3)
limit=0
if(num1<num2) and (num1<num3):
    limit=num1
elif (num2<num1)and (num2<num3):
    limit=num2
elif (num3<num1) and (num3<num2):
    limit=num3

for i in range(2,(limit+1)):
    if num1%i==0 and num2%i==0 and num3%i==0:
        hcf=i
print(hcf)




