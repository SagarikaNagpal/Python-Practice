def fibo(n):
    if n < 0:
        print('Wrong Input')
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
n = int(input('write the index'))
print()
print(fibo(n))


