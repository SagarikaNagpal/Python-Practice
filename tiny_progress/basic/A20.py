# Question A20: WAP to find out the greatest of three numbers using conditional operator.

def greatest(a,b,c):
    if a>b and a>c:
        print('A is Greatest')
    elif b>a and b>c:
        print('B is Greatest')
    else:
        print('C is greatest')

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
greatest(a,b,c)
