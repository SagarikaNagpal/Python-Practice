# Question B26: WAP to calculate the area of a circle, a rectangle or a triangle depending upon user’s choice.
# 		Choice					Area
# 		1					Circle  3.4*r^2
# 		2					Rectangle  wl
# 		3					Triangle hb/2
import math
choice=int(input("type ur choice: "))
r=2;
h=3;
b=4;
l=5;

if(choice==1):
    print((3.14*math.pow(r,2)),"ar of cirlcle")

elif(choice==2):
    print(b*l,"area of rect")

elif(choice==3):
    print((h*b)/2,"are of tringle")

