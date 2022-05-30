# Question A7: WAP to input 4 integers a, b, c, d 
# and check that the equation a3 + b3 +c3 = d3 is satisfied or not.

import math

a = int(input('a:'))
b = int(input('b:'))
c = int(input('c:'))
d = int(input('d:'))

print(pow(a,3)+pow(b,3)+pow(c,3))
print(pow(d,3))

if pow(a,3)+pow(b,3)+pow(c,3) == pow(d,3):
    print('True')
else:
    print('False')   