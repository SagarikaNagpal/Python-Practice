# Question B32: WAP to find out the sum and average of all the numbers within the given range.

def Sum_Average():
    n = int(input('How many numbers you want to add? '))
    total = 0
    count = 0

    for i in range(1,n+1):
        total += i
        count += 1
        average = total/n
        print(count)

    print('Sum: ',total)
    print('Average: ',average)

Sum_Average()


