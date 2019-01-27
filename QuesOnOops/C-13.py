# to input two strings and print which one is lengthier.

s1 = input("String1: ")
s2 = input("String2: ")

if(len(s1)>len(s2)):
    print("String -",s1,"-is greater than-", s2,"-")
else:
    print(s2,"is greater")