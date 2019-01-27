# Write a function that has two integer arguments and returns first number raised to the power second number.
import math
def power(a,b):

    num = math.pow(b,a)

    return num
a = int(input("a: "))
b = int(input("b: "))
print(power(a,b))