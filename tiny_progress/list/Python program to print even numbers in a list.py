def listCreate():
    n = int(input('Number of elements in list: '))
    l =[]
    for i in range(n):
        l.append(int(input('element is: ')))
    return l


def even(l):
    even = []
    for evenNum in l:
        if evenNum %2 == 0:
            even.append(evenNum)
    return even

def main():
    first = listCreate()
    second= even(l=first)
    print(f'even num  is {second}')
if __name__ == '__main__':
    main()
