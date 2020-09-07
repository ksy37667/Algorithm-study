# import sys
# from sys import stdin
# sys.setrecursionlimit(10**6) 

# dd = [(1,0), (-1,0), (0,1), (0,-1)]
# input = stdin.readline

# def check(array):
#     for i in range(n):
#         for j in range(m):
#             if array[i][j] != 0:
#                 return True
    
#     return False

# def dfs(x,y):
#     visited[x][y] = True

#     for a,b in dd:
#         dx = x+a
#         dy = y+b
#         if dx < 0 or dx >= n or dy <0 or dy >= m:
#             continue
#         if visited[dx][dy]:
#             continue
#         if array[dx][dy] != 0:
#             dfs(dx, dy)

    

# n,m = map(int, input().split(' '))
# array = [[] for _ in range(n)]
# save_cnt = [[0] * m for _ in range(n)]

# age = 0
# cnt = 0

# for i in range(n):
#     array[i] = list(map(int, input().split(' ')))


# while cnt < 2:
#     cnt = 0
#     age += 1
#     visited = [[False] * m for _ in range(n)]

#     for i in range(n):
#         for j in range(m):
#             if array[i][j] > 0:
#                 for x,y in dd:
#                     dx = i+x
#                     dy = j+y
#                     if dx < 0 or dx >= n or dy <0 or dy >= m:
#                         continue
#                     if array[dx][dy] == 0:
#                         save_cnt[i][j] += 1
    
#     for i in range(n):
#         for j in range(m):
#             if array[i][j] >= save_cnt[i][j]:
#                 array[i][j] -= save_cnt[i][j]
#             else:
#                 array[i][j] = 0
#             save_cnt[i][j] = 0

                    
#     for i in range(n):
#         for j in range(m):
#             if not(visited[i][j]) and array[i][j] != 0:
#                 dfs(i,j)
#                 cnt += 1

#     # print(printArray(array))

#     if not(check(array)):
#         age = 0
#         break
        

# print(age)

from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
q = deque()
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

for i in range(n):
    for j in range(m):
        if a[i][j] > 0:
            q.append((i, j))
        else:
            a[i][j] = -1

def bfs(i, j, check):
    bq = deque()
    bq.append((i, j))
    check[i][j] = True
    while bq:
        x, y = bq.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if check[nx][ny] is False and a[nx][ny] > 0:
                bq.append((nx, ny))
                check[nx][ny] = True

def counting():
    cnt = 0
    check = [[False]*m for _ in range(n)]
    for _ in range(len(q)):
        x, y = q.popleft()
        q.append((x, y))
        if check[x][y] is False:
            bfs(x, y, check)
            cnt += 1
            if cnt >= 2:
                return True
    return False

def melting():
    p = deque()
    for _ in range(len(q)):
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if a[x][y] > 0 and a[nx][ny] == -1:
                a[x][y] -= 1
        if a[x][y] > 0:
            q.append((x, y))
        elif a[x][y] == 0:
            p.append((x, y))
    while p:
        x, y = p.popleft()
        a[x][y] = -1

def solve():
    year = 0
    while q:
        melting()
        year += 1
        if counting() is True:
            return year
    return 0

print(solve())