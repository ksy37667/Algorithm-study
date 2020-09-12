import heapq
import sys
input = sys.stdin.readline

INF = sys.maxsize

def dijkstra(start, end, adj, n):
    if start == end:
        return 0
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    distance = [INF] * (n+1)

    distance[start] = 0
    cnt = 0

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

def solution(n, s, a, b, fares):
    adj = [[] for i in range(n+1)]
    for i in fares:
        adj[i[0]].append((i[1],i[2]))
        adj[i[1]].append((i[0],i[2]))
    answer = INF
    print(adj)
    for i in range(1, n+1):
        answer = min(answer, dijkstra(s, i, adj, n) + dijkstra(i,a,adj,n) + dijkstra(i,b,adj,n))
    return answer


n = 6
s = 4
a = 6
b = 2

fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

n = 7
s = 3
a = 4
b = 1

fares = 	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

n = 6
s = 4
a = 5
b = 6

fares = 	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
print(solution(n,s,a,b,fares))