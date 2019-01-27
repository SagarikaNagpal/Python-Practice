# Write a function that receives a string and a character as argument and returns 1 if the character is found in the string else returns 0.

def finding(str,ch):
    str = "hi ,watsup?"


    q= ch in str
    if(q==True):
        finds = str.find(ch)
        return finds

    else:
        return 0
ch = input("ch is: ")
print(finding(str,ch))




