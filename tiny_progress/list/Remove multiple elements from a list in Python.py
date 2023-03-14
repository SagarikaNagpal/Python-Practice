def listCreate():
    l = []
    n = int(input('Nuber of items: '))
    for i in range(n):
        l.append(int(input('only int, ele: ')))
    return l

def removing(l):
    newList = []
    for items in l:
        if items % 2 == 0:
            newList.append(items)
    return newList



def main():
    first = listCreate()
    print(f'{first} is the list ')
    sec = removing(l=first)
    print(f'{sec} is the list ')

if __name__ =='__main__':
    main()