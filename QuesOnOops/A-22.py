import math
input=int(input("input of a num is: "))
sq = int(math.pow(input,2))
cube = int(math.pow(input,3))
if(input%2==0):
    print(sq)
else:
    print(cube)