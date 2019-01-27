# Question B40: WAP to input 2 numbers and find out the sum of all the even numbers which are not
# divisible by 5 but divisible by 3 and lies between the given two numbers.
num1 = int(input("Please enter the number "))
num2 = int(input("Please enter the number "))

i = num1
sum = 1
while i < num2:
    if (i % 2 == 0 and i % 3 == 0 and i % 5 != 0):
        sum = sum + i
    i = i + 1
print("The sum of range numbers are ", sum)
