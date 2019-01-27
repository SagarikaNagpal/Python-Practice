# Write a function to print the sum and average of first n natural numbers where n is passed to the function as argument.

# def SumAndAverage(a):
#     n=0
#     sum = 0
#     avg = 0
#
#     for num in range(1,n+1):
#         sum = sum+num
#         print("sum is ",sum)
#
#         avg = sum/n
#
# a = input("number is: ")
#
# print(SumAndAverage(a))


# def natural(n):
#     sum=0
#     for values in range(0,n):
#         sum+=values
#     average = sum/n
#     print("The sum is ",sum)
#     print("The average is ",average)
#
#
# natural(4)


def natural(n):
    while(n!= 0):
        sum = 0
        for i in range(0,n+1):
          sum =sum+i

        return sum
n = int(input("num: "))
print(natural(n))