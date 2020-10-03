import heapq
import sys
N, M, X = list(map(int, input().split()))
INF = 1e9


graph = [[] for _ in range(N)]

for _ in range(M):
    a,b,c = list(map(int, input().split()))
    graph[a-1].append([b-1,c])


def dijkstra(graph, start, end):
    dist = [INF]*N
    dist[start] = 0
    queue = []

    heapq.heappush(queue, [dist[start], start])
    while queue:
        cost, cur = heapq.heappop(queue)

        if dist[cur] < cost:
            continue

        for adjacent, weight in graph[cur]:
            su = cost + weight
            if su < dist[adjacent]:
                dist[adjacent] = su
                heapq.heappush(queue, [dist[adjacent], adjacent])
        
    return dist[end]
        
result = []
for i in range(N):
    result.append(dijkstra(graph,X,i) + dijkstra(graph, i, X))



result.sort()
print(result)