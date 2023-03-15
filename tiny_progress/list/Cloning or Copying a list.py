def listCreate():
    l = []
    n = int(input('Nums in list: '))
    for i in range(n):
        l.append(int(input('Elements: ')))
    return l


def cloning(l):
    li1=l[:]
    return li1


def main():
    first = listCreate()
    print("list: ",first)
    second = cloning(l=first)
    print("list2 Copy is: : ", second)

if __name__ == '__main__':
    main()
