# to count the numbers of vowels, consonants, digits and special symbols in a given string.

s = (input("string: "))
count = 0
vowels = 0
consonants = 0
digits = 0
spcl_symbol = 0

for i in range(0,len(s)):
    ch = s[i]


    if((ch>= 'a' and ch<= 'z'  )or (ch >='A' and ch<='Z')):
        ch.lower()


        if(ch == 'a'or ch == 'e'or ch == 'i'or ch == 'o'or ch == 'u' ):
            vowels+=1


        else:
            consonants += 1


    elif(ch>=1 and ch<=9):
        digits+=1



    else:
        spcl_symbol+=1


print(vowels,"vowels")
print(consonants,"consonants")
print(digits,"digits")
print(spcl_symbol,"spcl_symbol")



