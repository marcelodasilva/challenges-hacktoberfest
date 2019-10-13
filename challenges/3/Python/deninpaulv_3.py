def fib(n):
    n1 = 0
    n2 = 1
    count = 0
    if n <= 0:
        print("error")
    elif n == 1:
        print(n1)
    else:
        while count < n:
            print(n1,end=' ')
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            count += 1

n = int(input())
fib(n)
