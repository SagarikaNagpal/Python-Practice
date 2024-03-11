# Question B33: WAP to print all the numbers falling between 2 numbers entered by the user.
# Question B36: WAP to print the sum and average of first n natural numbers.
# Question B37: WAP to print the sum and average of first n odd numbers.
# Question B38: WAP to print the sum and average of first n even numbers.



# WAP to print counting from 10 to 1.
'''def count_down():
    for i in range(10,0,-1):
        print(i,end = ', ' if i > 1 else '')
count_down()
'''''


# Question B31: WAP to print counting from 51 to 90.
"""
def counting():
    for i in range(51,91,1):
        print(i, end = ', ' if i < 90 else '')
counting()"""

# Question B32: WAP to find out the sum and average of all the numbers within the given range.
'''
def sum_avg(n):
    total_sum = sum(range(1,n+1))
    avg = total_sum/n
    print('Total Sum',total_sum)
    print('Total Average',avg)

n = int(input('n: '))
sum_avg(n)
'''

# Question B34: WAP to print all the even numbers between 1 and 50.
# Question B34: WAP to print all the even numbers between 1 and 50.
# Question B35: WAP to print all the odd numbers between 1 and 50.

'''def Num():
    print()
    print("EVEN: ")
    for i in range(1, 51):
        if i % 2 == 0:
            print(i, end=', ' if i < 50 else '')
    print()  # Print a newline to separate even and odd numbers
 
    print("ODD: ")

    for i in range(1, 51):
        if i % 2 != 0:
            print(i, end=', ' if i < 49 else '')  # No comma after the last odd number
    print()

Num()'''


# Question B36: WAP to print the sum and average of first n natural numbers.

'''
def naturalNum():
    normalSum = sum(range(0,n+1))
    normal_avg = normalSum/n
    print('Sum: ' ,normalSum)
    print('Avg: ',normal_avg)

n= int(input('n: '))
naturalNum()'''

# Question B37: WAP to print the sum and average of first n odd numbers.
'''def OddNum():
    totalSum = 0
    count = 0
    for i in range(0,n*2):
        if i%2 !=0:
            print(i)
            totalSum += i
            count += 1
    print("Total Sum: ",totalSum)
    average= totalSum/n
    print("Average",average)
n = int(input('n: '))
OddNum()
'''

# Question B38: WAP to print the sum and average of first n even numbers.

'''def even():
    totalSum = 0
    count = 0
    for i in range(1,n*2):
        if i %2 ==0:
            print(i)
            totalSum +=i
            count += 1
    print("Total Sum: ", totalSum)
    average = totalSum / n
    print("Average", average)


n = int(input('n: '))
even()'''

#Prime number:

'''def primeNum(num):
    if num == 1:
        print('The num is not prime')
    elif num > 1:
        divisors = []
        for i in range(2, num + 1):
            if num % i == 0:
                divisors.append(i)
        if len(divisors) == 1:
            print("num is prime")
        else:
            print("num is not prime")
            print("It is divisible by:", divisors)

num = int(input('Number: '))
primeNum(num)'''


# Question B39: WAP to print the table of a given number.
def table(num):

    for i in range(1, 11):
        result = num * i
        print(f'{num} * {i} = ', result)
num = int(input('Number: '))
table(num)


