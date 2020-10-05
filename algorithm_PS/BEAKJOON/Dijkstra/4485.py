import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

dd = [(1,0), (-1,0), (0,-1), (0,1)]

def dijkstra(sx,sy):
    cnt = 0
    heap_data = []
    heapq.heappush(heap_data, (cnt, sx, sy))
    visited[sx][sy] == True

    while heap_data:
        cnt, now_x, now_y = heapq.heappop(heap_data)
        if now_x == n-1 and now_y == n-1:
            return cnt

        for x, y in dd:
            dx, dy = now_x+x, now_y+y

            if dx < 0 or dx >=n or dy < 0 or dy >= n:
                continue
            if visited[dx][dy]:
                continue
            
            visited[dx][dy] = True

            if array[dx][dy] == '0':
                array[dx][dy] = '1'
                heapq.heappush(heap_data, (cnt + 1, dx, dy))
            else:
                heapq.heappush(heap_data, (cnt, dx, dy))


n = int(input())


visited = [[False] * n for _ in range(n)]

array = [[] * n for _ in range(n)]
for i in range(n):
    array[i] = list(input())[:-1]
    

print(dijkstra(0,0))