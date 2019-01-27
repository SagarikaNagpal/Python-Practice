arr= [1,2,3,4,5,6,7,8,9,10]

odd_count  = 0
even_count = 0
sum_even = 0
sum_odd = 0



for i in arr:

    if(i % 2 ==1):
        odd_count+= 1
        sum_odd+=i

    else:
        even_count+=1
        sum_even+=i

print(odd_count,"is odd count")
print(even_count,"even count")
print(sum_odd , "sum of odd")
print(sum_even ,"sum of even")