# https://www.geeksforgeeks.org/python-program-to-check-armstrong-number/

# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....

number = int(input('Number: '))
def armstrong(n):
    if n in range(1,10):
        return True
    a = len(str(n))
    sum = 0
    original = n
    while n>0:
        digit = n %10
        sum+= digit ** a
        n = n//10
    if sum == original:
        return True
    else:
        return False
if(armstrong(number)):
    print('Num is Armstrong')
else:
    print('Num is not Armstrong')


