from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(arr, visited, start, count):
    visited[start[0]][start[1]] = True
    queue = deque()
    queue.append(start)

    while queue:
        start = queue.popleft()

        for i in range(4):
            x = start[0] + dx[i]
            y = start[1] + dy[i]
            
            if x >= 0 and y >= 0 and x < N and y < M:
                if visited[x][y] == False and arr[x][y] == '1':
                    queue.append([x,y])
                    visited[x][y] = True
                    count[x][y] = count[start[0]][start[1]] + 1           
        

N, M = map(int, input().split(' '))
arr = []
visited = []
count = []
start = [0,0]

for i in range(N):
    arr.append(list(input()))
    visited.append([False]*M)
    count.append([0]*M)

count[0][0] = 1


bfs(arr, visited, (0,0), count)

print(count[N-1][M-1])
