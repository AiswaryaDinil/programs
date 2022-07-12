from functools import reduce
lst=[25,30,34,5,9]
str_lst=[str(n) for n in lst]
print(str_lst)

max_num=reduce(lambda n1,n2:(n1+n2) if (n1+n2)>(n2+n1) else (n2+n1),str_lst)
print(sorted(max_num))

