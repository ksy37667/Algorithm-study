from sys import setrecursionlimit
setrecursionlimit(10**9)

def dfs(i,j):
    if visited[i][j] < 0:
        visited[i][j] = 0
        for d in range(4):
            x, y = i + dx[d], j + dy[d]
            if 0 <= x < n and 0<= y <n and forest[i][j] < forest[x][y]:
                visited[i][j] = max(visited[i][j], dfs(x,y))
        visited[i][j] += 1
    return visited[i][j]
 

n = int(input()) 
forest = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

result = 0

for i in range(n):
    for j in range(n):
        result = max(result, dfs(i,j))
    
print(result)