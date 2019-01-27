# Write a function to calculate the area of a rectangle where length and breadth are passed to the function as argument.

def areaofrect(l,b):

    area = l*b
    return area

l = int(input("length: "))
b = int((input("breadth: ")))

print(areaofrect(l,b))