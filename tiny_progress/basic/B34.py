# Question B34: WAP to print all the even numbers between 1 and 50.


n = int(input('What would be the range? '))
def even(n):
    a = [i for i in range(1,n+1) if i%2 == 0]
    print(f'Even numbers are : {a}')
even(n)


def odd(n):
    b = [i for i in range(1,n+1) if i%2 != 0]
    print(f'Odd numbers are : {b}')
odd(n)