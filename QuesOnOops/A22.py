#Question A22: WAP to input a number. If the number is even, print its square otherwise print its cube.
import math
a=int(input("num: "))
sq = int(math.pow(a,2))
cube =int (math.pow(a,3))

if a%2==0:
    print("sq of a num is ",sq)

else:
    print(cube)