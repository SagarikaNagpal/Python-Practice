def createlist():
    '''
    :return: l that has been created in further steps
    '''
    l = []
    n = int(input('Numbers in the list: '))
    for i in range(n):
        l.append(int(input("Items are: ")))
    return l

def multiple(l):
    '''
    :param l:
    :return: k
    '''
    multiplication = 1
    for k in range (len(l)):
        multiplication = multiplication * l[k]
    return multiplication

def main():
    firstProg = createlist()
    print(f'{firstProg} is the list')
    secondProg = multiple(l=firstProg)
    print(f'{secondProg} is the multiplication')

if __name__ == '__main__':
    main()