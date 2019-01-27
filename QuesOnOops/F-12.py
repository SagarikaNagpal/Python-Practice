# Write a function that returns the factorial of a number where number is passed to the function as argument

def fact(a):
    facto = 1
    for i in range(1,a+1):
        facto= facto*i
    return facto


print(fact(5))

