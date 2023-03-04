
def prime(num):
    num = int(input("Num: "))
    if num >1 :
        for i in range(2,num):
            if(num%i ==0):
                print(num,'is not a prime number')
                break
        else:
            print(num,'Num is a prime number')
    else:
        print("Num is not a  prime numm")
