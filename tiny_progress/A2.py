# Question A2: WAP to input roll number, name and marks of a student in 5 subjects and 
# calculate the total and average marks. Display all the values
import math

from numpy import average
roll_num = int(input('Roll Number: '))
name = input('Name: ')
m1 = int(input('Eng '))
m2 = int(input('Hin '))
m3 = int(input('Maths '))
m4 = int(input('SST '))
m5 = int(input('Sci '))

sum = m1+m2+m3+m4+m5
avg = sum/len(str(sum))
print('Sum: ',sum)
print('Avg: ',avg)
