n = int(input())

def fib(n):
    fiblist = []
    if n <= 1:
        fiblist[0]=0
        return
    else:
        fiblist[n-1] = fib(n-1) + fib(n-2)

print(fib(n))

