# mathope->operat.py=>add,sub.cube

# testdemo=demo.py
from flowcontrolls.fordemo import is_prime
from mathoperations.operations import *
print(add(10,20))
print(cube(3))



def prime_range(low,upp):#10,,,50
    for num in range(low,(upp+1)):
        if is_prime(num):
            print(num)
