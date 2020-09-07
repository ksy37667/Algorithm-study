import heapq
import sys
input = sys.stdin.readline

INF = sys.maxsize

def dijkstra(start, end):
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    distance = [INF] * (n+1)

    distance[start] = 0
    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distance[now] < dist:
            continue
        
        for i in adj[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap_data, (cost, i[0]))
    
    return distance[end]

n, e = map(int, input().split(' '))
adj = [[] for _ in range(n+1)]

for _ in range(e):
    a,b,c = map(int, input().split(' '))

    adj[a].append((b,c))
    adj[b].append((a,c))

v1,v2 = map(int, input().split(' '))


result1 = dijkstra(1, v1) + dijkstra(v1,v2) + dijkstra(v2, n)
result2 = dijkstra(1, v2) + dijkstra(v2,v1) + dijkstra(v1, n)


if result1 >= INF and result2 >= INF:
    print(-1)
else:
    print(min(result1, result2))


