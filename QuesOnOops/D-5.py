# Question D5: WAP to calculate the average of 10 values stored in an array and display
#  all those values which are more than the calculated average.

arr = [1,2,3,4,5,6,7,8,9,10]
for val in arr:
    add = sum(arr)
    avg = add/10
print(add)
print(avg)

for i in arr:
    if(i>avg):
        print(i)