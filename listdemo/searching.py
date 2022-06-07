# linear search

arr=[1,2,13,14,15,16,65,78,89]
element=14
flag=0
# for i in range(len(arr)):
#     if arr[i] ==element:
#         flag=1
#         break
# print("element found" if flag!=0 else "not found")

for num in arr:
    if num ==element:
        flag=1
        break
print("element found" if flag!=0 else "not found")





