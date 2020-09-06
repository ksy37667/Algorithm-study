cache = [0] * 46

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if cache[x] != 0:
        return cache[x]
    cache[x] = fibo(x-1) + fibo(x-2)
    return cache[x]


n = int(input())
print(fibo(10))
