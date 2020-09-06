n,k = map(int, input().split(' '))

cache = [[0]* (k+1) for _ in range(n+1)]


for i in range(1, n+1):
    w, v = map(int, input().split())

    for j in range(1, k+1):
        if j < w:
            cache[i][j] = cache[i-1][j]
        else:
            cache[i][j] = max(cache[i-1][j], cache[i-1][j-w] + v)
        

print(cache[n][k])
