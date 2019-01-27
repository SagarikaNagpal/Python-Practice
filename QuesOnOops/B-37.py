# Question B37: WAP to print the sum and average of first n odd numbers.
n = int(input("write a num: "))
sum=0
avrg = 0
for num in range(0,n+1):
  sum=sum+num
  if(sum%2==1):
    print("sum of " ,num ,"are: ",sum)
    avrg= sum/n
    print("avrg of sum is: ",avrg)


