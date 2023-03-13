# Python program to find smallest number in a list

def listCreate():
    n = int(input('Number of elements in list: '))
    l =[]
    for i in range(n):
        l.append(int(input('element is: ')))
    return l

def Smallsorting(l):
    l.sort()
    return l[0]

def Largesorting(l):
    l.sort()
    return l[-1]

def SecondLargesorting(l):
    l.sort()
    return l[-2]

def NLargesorting(l):
    l.sort()
    k = int(input('From which digit: '))
    return l[-k:]

def main():
    first = listCreate()
    # second = Smallsorting(l=first)
    # print(f'list is{first}')
    # print(f'second is {second}')
    # third = Largesorting(l=first)
    # print(f'third is {third}')
    # fourth = SecondLargesorting(l=first)
    # print(f'Second Large sorting is {fourth}')
    fifth = NLargesorting(l=first)
    print(f'n largest is {fifth}')
if __name__ == '__main__':
    main()


