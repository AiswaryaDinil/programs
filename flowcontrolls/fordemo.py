




def is_prime(num):
    flag=0
    for i in range(2,num):
        if(num%i==0):
            flag=1
            break
    return flag == 0



def prime_range(low,upp):#10,,,50
    for num in range(low,(upp+1)):
        if is_prime(num):
            print(num)





# flowcontrolls(if..else,elif,  for,while)
#functions ,lambda function
# ================================================
#git and github

# listdemo set tuple,dictionary
