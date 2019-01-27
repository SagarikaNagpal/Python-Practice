# to count the lower case and upper case letters in a string.
s = input("string: ")
lower = 0
upper =0


for i in range(0,len(s)):
    ch = s[i]
    if(ch>='a' and ch<= 'z'):
        lower +=1


    elif(ch>='A' and ch<= 'Z'):
        upper +=1


print(lower,"lower")
print(upper,"upper")