n, m = map(int, input().split())
array = []
 
for i in range(n):
    s = input()
    array.append(list(map(int, list(s))))
 
cache = [[0] * (m+1) for _ in range(n + 1)]
side = 0
 
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if array[i - 1][j - 1]:
            cache[i][j] = min(cache[i][j - 1], cache[i - 1][j], cache[i - 1][j - 1]) + 1
 
            if cache[i][j] > side:
                side = cache[i][j]
 
print(side**2)