# Write a function to calculate the area of a circle where radius is passed to the function as argument.

def area_of(r):

    area= 3.14*r*r
    return area

r = int(input("radius: "))
print(area_of(r))