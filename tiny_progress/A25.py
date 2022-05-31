# Question A25: WAP to swap the values of two integer variables
# Using extra variable
# Without using extra variable


from calendar import c


print('No extra variable')

a= 25
b = 12
print( a,b )
# a,b = b,a
print("Final are from :", a,b )

# Using extra variable 

c = a
a = b
b = c

print("Final from extr variables :", a,b,c )
print('{0},{1}'.format(a,b))

