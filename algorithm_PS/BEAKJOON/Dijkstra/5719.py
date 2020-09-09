import heapq
import sys
from collections import deque
input = sys.stdin.readline

def dijkstra(start, end):
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    distance[start] = 0

    while heap_data:
        dist, now = heapq.heappop(heap_data)

        if distance[now] < dist:
            continue
        for e in adj[now]:
            cost = dist + e[1]
            if distance[e[0]] > cost and visited[now][e[0]] == False:
                distance[e[0]] = cost
                heapq.heappush(heap_data, (cost, e[0]))

def bfs(start, end):
    queue = deque()
    queue.append(end)
    while queue:
        now = queue.popleft()
        if now == start:
            continue
        
        for e in adj_tmp[now]:
            if distance[now] == distance[e[0]] + e[1]:
                visited[e[0]][now] = True
                queue.append(e[0])


while True:
    n, m = map(int, input().split(' '))
    if n == 0 and m == 0:
        break
    
    s, d = map(int, input().split(' '))
    adj = [[] for _ in range(n)]
    adj_tmp = [[] for _ in range(n)]

    for _ in range(m):
        u, v, p = map(int, input().split(' '))
        adj[u].append((v,p))
        adj_tmp[v].append((u,p))

    
    distance = [1e9] * n
    visited = [[False]* n for _ in range(n)]
    dijkstra(s, d)
    bfs(s, d)  
    distance = [1e9] * n
    dijkstra(s,d)

    print(distance[d] if distance[d] != 1e9 else -1)