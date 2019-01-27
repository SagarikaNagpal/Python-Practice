# Write a function to print the sum and average of first n odd numbers where n is passed to the function as argument.

def natural(n):
    sum = 0
    for values in range(0,n+1):

        if(values%2 ==1):

            sum = sum + values
    return sum

n = int(input("n: "))
print(natural(n))
