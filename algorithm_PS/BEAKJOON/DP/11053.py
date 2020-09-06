n = int(input())
array = list(map(int, input().split()))
cache = [1] * n


for i in range(1,n):
    for j in range(0,i):
        if array[j] < array[i]:
            cache[i] = max(cache[j]+1, cache[i])

print(max(cache))
