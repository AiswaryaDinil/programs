f=open("abc.txt","w")

lst=["python","JS","C#"]
for lan in lst:
    lan+="\n"
    f.write(lan)