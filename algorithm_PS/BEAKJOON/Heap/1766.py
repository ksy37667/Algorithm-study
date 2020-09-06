# https://www.acmicpc.net/problem/1766
# 위상정렬

import heapq

N, M = map(int, input().split(' '))

array = [[] for _ in range(N+1)]
degree = [0] * (N+1)

for _ in range(M):
    x,y = map(int, input().split(' '))
    array[x].append(y)
    degree[y] += 1

queue = []
result = []

for i in range(1, n+1):
    if degree[i] == 0:
        heapq.heappush(queue, i)


while queue:
    data = heapq.heappop(queue)
    result.append(data)
    for i in array[data]:
        degree[i] -= 1
        if degree[i] == 0:
            heapq.heappush(queue, i)
    

for i in result:
    print(i, end=' ')