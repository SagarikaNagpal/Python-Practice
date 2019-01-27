# Write a function that prints the sum of the digits, count of the digits and
# reverse of a number. Number is passed to the function as argument.

def digitAction(n):
    sum = 0
    count = 0
    while (n != 0):

        count = count + 1
        n= n//10
    return count

    while(n!= 0):
        sum = sum + int(n % 10)
        n = int(n / 10)

    return (sum)



n = 687
print(digitAction(n))
