n1 = int(input("1: "))

n2 = int(input("2: "))

times = int(input('how amny timeu want: '))

print(n1,n2, end=" ")

while(times-2):

    ser = n1+n2
    n1 = n2
    n2 = ser

    print(ser,end=" ")

    times=times-1
