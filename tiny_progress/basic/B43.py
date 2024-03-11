# Question B43: WAP to print the factorial of a given number.

'''Factorial is a mathematical operation represented by the symbol
"!". It's used to find the product of all positive integers less than or equal to a given positive integer.
For example, the factorial of 5 is denoted as "5!" and calculated as follows:
5!= 5*4*3*2*1 = 120'''

# with list comprehension :
import math
n = int(input('Facorial of: '))
def factorial():
    f = print(f'The factorial of {n} is : {math.prod([i for i in range(2,n+1)])}')
factorial()

# without list comprehension:


def factor():
    if n<=1:
        print('number should be greater than 1! ')
    else:
        factorial = 1
        for i in range(2,n+1):
            factorial *=i
        print(f'Factorial of {n} is {factorial}')
factor()