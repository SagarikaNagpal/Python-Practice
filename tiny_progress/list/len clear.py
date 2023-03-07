def listCreate():
    l = []
    n = int(input("How many items in list: "))
    for i in range(n):
        l.append(int(input('Numbers as items are: ')))

    print(l)
    print(f'Length of list : {len(l)}')
    return l
def clearProg(l):
    l.clear()

    return l

def main():
    firstProg = listCreate()
    secondProg = clearProg(l=firstProg)
    print(secondProg)

if __name__ == '__main__':
    main()