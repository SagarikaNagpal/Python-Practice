def listCreate():
    l = []
    n = int(input('Nums in list: '))
    for i in range(n):
        l.append(int(input('Elements: ')))
    return l


def counting(l):
    x = int(input("Which number you want to count: "))
    count = 0
    for ele in l:
        if ele == x:
            count = count + 1
    return count


def main():
    first = listCreate()
    print("list: ",first)
    second = counting(l=first)
    print("Counting of a number is: : ", second)

if __name__ == '__main__':
    main()
