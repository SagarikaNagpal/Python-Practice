#  WAP to print the sum and average of first n natural numbers.
n =int( input("Enter Number to calculate sum:"))
average = 0
sum = 0
for num in range(0,n+1):
    sum = sum+num

print("SUM of first ", n, "number is: ", sum )

average=sum/n
print("the avg of num",average)