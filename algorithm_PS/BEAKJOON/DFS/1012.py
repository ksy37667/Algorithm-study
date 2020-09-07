import sys
sys.setrecursionlimit(100000)

T = int(input())

dd = [(1,0), (0,1), (0,-1), (-1,0)]

def dfs(vx, vy):
    visited[vx][vy] = True

    for x, y in dd:
        dx = x + vx
        dy = y + vy

        if dx < 0 or dx >= N or dy < 0 or dy >= M:
            continue
        if visited[dx][dy] or array[dx][dy] == 0:
            continue
        dfs(dx,dy)


for _ in range(T):
    N, M, K = map(int, input().split(' '))
    cnt = 0

    array = [[0]* M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        array[x][y] = 1

    
    for i in range(N):
        for j in range(M):
            if array[i][j] == 1 and not(visited[i][j]):
                dfs(i,j)
                cnt += 1
    
    print(cnt)