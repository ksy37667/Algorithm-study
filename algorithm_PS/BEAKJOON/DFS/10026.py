import copy
import sys
sys.setrecursionlimit(10**6) 

dd = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(i,j,array, rgb):
    visited[i][j] = True

    for x,y in dd:
        dx = i + x
        dy = j + y
        if (0 <= dx < N) and (0 <= dy < N):
            if not(visited[dx][dy]):
                if rgb == array[dx][dy]:
                    dfs(dx,dy,array,rgb)

# def dfs(sx, sy, array, color):
#     visited[sx][sy] = 1

#     for x,y in dd:
#         dx = sx + x
#         dy = sy + y
#         if(dx < 0 or dx >= N or dy < 0 or dy >= N):
#             continue
#         if visited[dx][dy]:
#             continue
#         if(array[dx][dy] == color):
#             dfs(dx, dy, array,color)



    

N = int(input())
array1 = [[] for _ in range(N)]
visited = [[False] * N for _ in range(N)]
cnt1, cnt2 = 0, 0

for i in range(N):
    array1[i] = list(input())

array2 = copy.deepcopy(array1)

for i in range(N):
    for j in range(N):
        if array2[i][j] == 'R':
            array2[i][j] = 'G'

for i in range(N):
    for j in range(N):
        if not(visited[i][j]):
            dfs(i,j,array1, array1[i][j])
            cnt1 += 1
            

visited = [[False] * N for _ in range(N)]   

for i in range(N):
    for j in range(N):
        if not(visited[i][j]):
            dfs(i,j,array2, array2[i][j])
            cnt2 += 1

print(cnt1, cnt2)