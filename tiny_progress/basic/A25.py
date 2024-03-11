# Question A25: WAP to swap the values of two integer variables
# (a)	Using extra variable
# (b)	Without using extra variable

a,b = 2,3
print(a,b)
b, a = a,b
print(a,b)

print('*************')
c = a
a = b
b = c
print(a,b)