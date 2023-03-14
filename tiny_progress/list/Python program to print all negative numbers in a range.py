def listCreate():
    l = []
    n = int(input('Nums in list: '))
    for i in range(n):
        l.append(int(input('Elements: ')))
    return l

def negativeNum(l):
    numList = []
    for i in l:
        if i <= 0:
            numList.append(i)
    return numList

def main():
    first = listCreate()
    print("list: ",first)
    second = negativeNum(l=first)
    print("list2: ", second)

if __name__ == '__main__':
    main()


