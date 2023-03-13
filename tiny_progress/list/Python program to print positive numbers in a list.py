def createList():
    l = []
    numOfItems = int(input('Number of Items in a list: '))
    for i in range(numOfItems):
        l.append(int(input('element is: ')))
    return l


def positiveNum(l):
    nL = []
    for num in l:
        if num >= 0:
            nL.append(num)
    return nL


def main():
    first = createList()
    print("list: ",first )
    second = positiveNum(l=first)
    print("list2: ", second)

if __name__ == '__main__':
    main()


