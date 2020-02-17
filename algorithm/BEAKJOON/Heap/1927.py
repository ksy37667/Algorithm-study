# https://www.acmicpc.net/problem/1927

import heapq

N = int(input())

queue = []
result = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if queue:
            result.append(heapq.heappop(queue))
        else:
            result.append(0)
    else:
        heapq.heappush(queue, x)


for data in result:
    print(data)