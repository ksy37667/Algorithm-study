import heapq

def dijkstra(start, adj, distance):
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
    return distance


def solution(n, edge):
    adj = [[] for _ in range(n+1)]
    distance = [1e9] * (n+1)
    for i in edge:
        adj[i[0]].append((i[1],1))
        adj[i[1]].append((i[0],1))

    result = sorted(dijkstra(1, adj, distance), reverse=True)
    cnt = 0

    for i in range(1, len(result)):
        if result[i] != result[i+1]:
            break
        elif result[i] == 1e9:
            continue
        else:
            cnt+=1

    print(cnt+1)


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
