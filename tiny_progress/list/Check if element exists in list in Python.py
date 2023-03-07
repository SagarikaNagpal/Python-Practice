def listCreation():
    listcreate = []
    n = int(input("How many items in list: "))
    for i in range(n):
        listcreate.append(int(input("enter item: ")))
        # print(listcreate)
    return listcreate


def checkElement(listcreate):
    i = int(input('num to check: '))
    if i in listcreate:
        return True
    else:
        print("Element is not in list")


def main():
    firstProg = listCreation()
    secondProg = checkElement(listcreate=firstProg)


if __name__ == '__main__':
    main()
