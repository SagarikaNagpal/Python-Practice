# Write a function to compare two strings. The strings must be passed to the function as argument.
# The function should return 0 if the strings are equal else returns 1.

def comparison(a,b):
    if(len(a)>len(b)):
        print(a)
        return 1
    elif(len(a)<len(b)):
        print(b)
        return 1
    else:
        return 0
a = input("a: ")
b = input("b: ")

print(comparison(a,b))