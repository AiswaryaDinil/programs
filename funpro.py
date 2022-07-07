from functools import reduce

lst=[10,3,30,4,5,8]

squares=list(map(lambda n:n**2,lst))
print(squares)


# num_out=[n-1 if n<5 else n+1 for n in lst]

# num_out=list(map(lambda n:n+1 if n>5 else n-1,lst))
# print(num_out)

gt_ten=list(filter(lambda n:n>10,lst))
print(gt_ten)
even=list(filter(lambda n:n%2==0,lst))
print(even)

sum=reduce(lambda n1,n2:n1+n2,lst)
print(sum)

product=reduce(lambda n1,n2:n1*n2,lst)
print(product)

max_no=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
print(max_no)