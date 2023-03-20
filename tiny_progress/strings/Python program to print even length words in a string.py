def evenLength(s):
    n = s.split(' ')
    for i in n:
        if len(i)%2 ==0:
            print(i)

evenLength(s = input('String: '))
