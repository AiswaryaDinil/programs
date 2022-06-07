# numbers=[12,13,14,15,16]
# for num in numbers:
#     if num%2==0:
#         print(num)

# for num in numbers:
#     if num>15:
#         print(num+1)
#     elif num<15:
#         print(num-1)
#     elif num==15:
#         print(num)

# count=0
# for num in numbers:
#     if num >=14 and num <=18:
#         count+=1
# print(count)

n_count=0
p_count=0
z_count=0
numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]
for num in numbers:
    if num >0:
        p_count+=1
    elif num <0:
        n_count+=1
    elif num ==0:
        z_count+=1
print(f"+ve count {p_count},-ve count {n_count},zero count {z_count}")


# numbers=[12,13,14,15,16,17,18]
# sum=0
# for n in numbers:
#     sum+=n
# print(sum)

