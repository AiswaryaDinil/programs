f=open("abc.txt")

lst=[line.rstrip("\n") for line in f]
print(lst)

# line=list(f)
# for line in f:
#     print(line)
