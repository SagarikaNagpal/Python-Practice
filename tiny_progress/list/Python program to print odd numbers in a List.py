def listCreate():
    n = int(input('Number of elements in list: '))
    l =[]
    for i in range(n):
        l.append(int(input('element is: ')))
    return l


def odd(l):
    odd = []
    for i in l:
        if i%2 ==1:
            odd.append(i)
    return odd


def main():
    first = listCreate()
    second= odd(l=first)
    print(f'odd num  is {second}')
if __name__ == '__main__':
    main()

