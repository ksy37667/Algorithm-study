import sys
import heapq

dd = [(1,0), (-1,0), (0,-1), (0,1)]

# 다익스트라 함수
def dijkstra(sx,sy):
    heap_data = []
    heapq.heappush(heap_data, (0, sx, sy))
    visited[sx][sy] == True

    while True:
        # cnt = 어두운 방을 밝은 방으로 바꾼 횟수
        # now_x, now_y 현재 위치 x,y 좌표
        cnt, now_x, now_y = heapq.heappop(heap_data)

        # 목표지점에 도착하면 cnt(어두운 방에서 밝은 방으로 바꾼 횟수)를 반환한다.
        if now_x == n-1 and now_y == n-1:
            return cnt

        for x, y in dd:
            dx, dy = now_x+x, now_y+y
            
            # 미로의 범위를 벗어나는 경우는 무시한다.
            if dx < 0 or dx >=n or dy < 0 or dy >= n:
                continue
            
            # 이미 한번 방문한 방은 무시한다.
            if visited[dx][dy]:
                continue

            # 현재 방문한 방을 True로 바꾸어준다.
            visited[dx][dy] = True
            
            # 현재 방문한 방이 밝은 방일 경우엔 힙에 cnt값을 그대로 넣어주고
            # 현재 방문한 방이 어두운 방일 경우 밝은 방으로 바꾸어주고 힙에 cnt + 1을 넣어준다. 
            if array[dx][dy] == '0':
                array[dx][dy] = '1'
                heapq.heappush(heap_data, (cnt + 1, dx, dy))
            else:
                heapq.heappush(heap_data, (cnt, dx, dy))

n = int(input())

visited = [[False] * n for _ in range(n)]

array = [[] * n for _ in range(n)]
for i in range(n):
    array[i] = list(input())
    

print(dijkstra(0,0))