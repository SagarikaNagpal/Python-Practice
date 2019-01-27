arr = []

s = int(input("size: "))

for a in range(0,s):
    arr.append(int(input("input is: ")))

print(arr)

for a in arr:
    if(a%2 == 0):
        print("evens are: ",[a])


    else:
        print("odds are:",[a])
