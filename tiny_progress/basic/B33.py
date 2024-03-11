# Question B33: WAP to print all the numbers falling between 2 numbers entered by the user.

def num():
    start = int(input("Starting number for range is : "))
    end = int(input("Ending number for range is : "))

    numbers = [i for i in range(start+1,end)]
    print(numbers)

num()


