# Question A15: WAP to input two numbers and print the greatest using conditional operator.

def two_number(a,b):
    if a > b:
        print(f'{a} is greater than {b}')
    else:
        print(f'{b} is greater than {a}')

a = float(input('a: '))
b = float(input('b: '))
two_number(a,b)