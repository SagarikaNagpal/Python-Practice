import math

def sqAndCube(n):
    sqsum =0
    cubeSum = 0

    for i in range(1,n+1):
        sqsum= sqsum+pow(i,2)
        cubeSum = cubeSum + pow(i, 3)
    print(f"{sqsum} is the sum of squares")
    print(f"{cubeSum} is the cube of squares")

n = int(input('n: '))

print(sqAndCube(n))

