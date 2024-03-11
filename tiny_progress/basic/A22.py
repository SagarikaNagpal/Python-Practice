# Question A22: WAP to input a number. If the number is even, print its square otherwise print its cube.

import math

def number(n):
    a = int(input('Enter number: '))
    if a%2 == 0:
        print('Sq ',math.pow(n,2))
    else:
        print('Cube ',math.pow(n, 3))
n = int(input('n: '))
number(n)

