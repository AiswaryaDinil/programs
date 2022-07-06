# try => block for doubtful code
# expect => block for handling code
# raise => key word to throw custom error
# finally => block for clean up processing

# n1=int(input("Enter 1st no:"))
# n2=int(input("Enter 2nd no:"))
# try:
#     res=n1/n2
#     print(f"result {res}")
# except Exception as e:
#     print(e)
#     n2=int(input("Enter a non zero no:"))
#     if n2 != 0:
#         res = n1 / n2
#         print(f"result {res}")
#
# finally:
#     print("line1")
#     print("line2")

# age=int(input("Enter age:"))
# if(age<18):
#     raise Exception("Not eligble for taking booster dose")
# else:
#     print("Eligible")

phn_no=input("Enter your phn no:")
if(len(phn_no)!=10):
    raise Exception("incorrect phn no")
else:
    print(f"vallid {phn_no}")