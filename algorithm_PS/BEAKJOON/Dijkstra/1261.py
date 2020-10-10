import heapq

M ,N = list(map(int, input().split()))
array = []

for i in range(N):
    array.append(list(input()))

visit = [[0 for _ in range(M)] for _ in range(N)]

def dijkstra(start, array, visit):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    queue = []
    heapq.heappush(queue,start)

    while queue:
        dist, x, y = heapq.heappop(queue)
        visit[x][y] = 1

        if x == N-1 and y == M-1:
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                visit[nx][ny] = 1
                if array[nx][ny] == "0":
                    heapq.heappush(queue, [dist,nx,ny])
                elif array[nx][ny] == "1":
                    heapq.heappush(queue, [dist+1,nx,ny])

print(dijkstra([0,0,0],array,visit))