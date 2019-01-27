# a=int(input("Enter the first number of the series "))
# b=int(input("Enter the second number of the series "))
# n=int(input("Enter the number of terms needed "))
# print(a,b,end=" ")
# while(n-2):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=" ")
#     n=n-1
n1 = int(input("1st: "))

n2 = int(input("2nd: "))

how_many = int(input("time of seq" ))
print(n1,n2,end=" ")

while(how_many-2):
    series = n1+n2
    n1=n2
    n2=series
    print(series,end=" ")
    how_many=how_many-1
