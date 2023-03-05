# Python Program for How to check if a given number is Fibonacci number?
import math


def isPerfectsq(num):
    s = int(math.sqrt(num))
    return s * s == num


def isFibo(num):
    if isPerfectsq(5 * (num ** 2) + 4) or isPerfectsq(5 * (num ** 2) - 4):
        print(f"{num} is a fibonacci number")
        return True
    else:
        print(f"{num} is not a fibonacci number")

num = int(input('num: '))
if (isFibo(num)) == True:
    print("Yes!")
else:
    print("Next attempt please!")
