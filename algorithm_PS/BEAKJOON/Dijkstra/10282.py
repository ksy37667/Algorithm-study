import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    distance[start] = 0

    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distance[now] < dist:
            continue
        for e in adj[now]:
            cost = dist + e[1]
            if distance[e[0]] > cost:
                distance[e[0]] = cost
                heapq.heappush(heap_data, (cost, e[0]))
        


for _ in range(int(input())):
    n, m, start = map(int, input().split(' '))
    adj = [[] for i in range(n+1)]
    distance = [1e9] * (n+1)

    for _ in range(m):
        x, y, cost = map(int, input().split(' '))
        adj[y].append((x,cost))
    
    dijkstra(start)
    count = 0
    max_distance = 0
    
    for i in distance:
        if i != 1e9:
            count += 1
            if i > max_distance:
                max_distance = i
    
    print(count, max_distance)
