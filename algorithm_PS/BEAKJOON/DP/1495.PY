n, s, m = map(int, input().split(' '))
array = list(map(int, input().split(' ')))

cache = [[0] * (m+1) for _ in range(n+1)]
cache[0][s] = 1

for i in range(1, n+1):
    for j in range(m+1):
        if cache[i-1][j] == 0:
            continue
        if j-array[i-1] >= 0:
            cache[i][j-array[i-1]] = 1
        if j+array[i-1] <= m:
            cache[i][j+array[i-1]] = 1


result = -1
for i in range(m, -1, -1):
    if cache[n][i] == 1:
        result = i
        break

print(result)