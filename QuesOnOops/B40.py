# Question B40: WAP to input 2 numbers and find out the sum of all the even numbers which are not
# divisible by 5 but divisible by 3 and lies between the given two numbers.

a = int(input("a: "))
b = int(input("b: "))

sum = 0

while a<b:
    if(a %2== 0 and a%3 == 0 and a%5!=0):
        sum = sum+a
        a=a+1
print(sum
