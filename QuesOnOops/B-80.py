# sum of  digit


n = int(input("num: "))
sum = 0

while(n>0):

    digit = n % 10

    sum = sum +digit

    n = n//10

print(sum, "is the total of digits")
