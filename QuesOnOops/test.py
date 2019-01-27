#Write a Python program to count the number 4 in a given list

list = [1,2,3,7,7,7,4,4,4]
count_4 =0
count_7 =0
for i in list:
    if(i==4):
        count_4 +=1
for o in list:
    if(o == 7):
        count_7 +=1

print("num of 4 is: ",count_4)
print("num of 7 is: ",count_7)
