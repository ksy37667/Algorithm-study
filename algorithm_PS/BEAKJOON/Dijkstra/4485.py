import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

dd = [(1,0), (-1,0), (0,-1), (0,1)]

def dijkstra(sx,sy):
    heap_data = []
    heapq.heappush(heap_data, (array[sx][sy], sx, sy))
    distance[sx][sy] = array[sx][sy]

    while heap_data:
        dist, now_x, now_y = heapq.heappop(heap_data)
        if distance[now_x][now_y] < dist:
            continue
        for x, y in dd:
            dx, dy = now_x+x, now_y+y

            if dx < 0 or dx >=n or dy < 0 or dy >= n:
                continue

            cost = dist + array[dx][dy]
            if distance[dx][dy] > cost:
                distance[dx][dy] = cost
                heapq.heappush(heap_data, (cost, dx, dy))
    return distance[n-1][n-1]

cnt = 1
while True:
    n = int(input())
    if n == 0:
        break

    array = [[] * n for _ in range(n)]
    distance = [[INF]*n for i in range(n)]
    for i in range(n):
        array[i] =list(map(int, input().split(' ')))
        
    
    print("Problem",cnt, end="")
    print(':', dijkstra(0,0))

    cnt += 1