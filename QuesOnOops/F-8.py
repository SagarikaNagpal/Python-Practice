# Write a function that has one integer argument and returns 0 if number is even else returns 1.

def OddEven(n):

    n= 0
    if(n%2)==0:
        print("even")
        # return
    else:
        print("odd")
        # return n

n = int(input("n: "))
print(OddEven(n))