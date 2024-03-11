# Question A3: WAP to find out the square of a given number.
# Question A4: WAP to input a number and print its cube.
# Question A5: WAP to input radius and calculate the area =  and circumference of a circle.
# Question A6: WAP to input length and breadth of a rectangle and calculate the area and perimeter.


import math
"This is answer A3 and A4"

# def square(num):
#     print('Number: ', num)
#     sq = math.pow(num,2)
#     print(sq)
# square(2)

"This is answer A5 and A6: A=π×r and circumference = C=2×π×r"

def A(r):
    area = round(math.pi* math.pow(r,2),2)
    print('Area:',area)
    cicumference = round(2*math.pi * r)
    print('cicumference:',cicumference)
r = int(input("Radius: "))
A(r)

