# Question A21: WAP to input choice (1 or 2). If choice is 1 print the area of a circle otherwise
# print the circumference of circle. Input the radius from user.
import datetime
import math
def circle(r):
    a = int(input('Press either 1: Area of Circle or 2: Circumference of circle: '))

    if a ==1:
        print('Area of circle: ', round(math.pi * pow(r,2),2))
    else:
        print('Circumference of circle: ', round(2*math.pi * r,2))

r = int(input('r: '))
circle(r)


