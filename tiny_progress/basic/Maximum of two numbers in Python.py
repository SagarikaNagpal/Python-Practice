# https://www.geeksforgeeks.org/maximum-of-two-numbers-in-python/

def greaterNum(a,b):
    if a>b:
        return(a,'is greater than',b)
    elif a==b:
        return(a,'is equal to ',b)
    else:
        return(b,'is greater than ',a)

a = int(input('a: '))
b = int(input('b: '))
print(greaterNum(a, b))

