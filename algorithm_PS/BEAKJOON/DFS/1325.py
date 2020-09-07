# import sys
# sys.setrecursionlimit(100000)

# def dfs(v):
#     visited[v] = True
#     global cnt
#     for i in adj[v]:
#         if not(visited[i]):
#             dfs(i)
#             cnt+=1

from collections import deque

def bfs(v):
    q = deque([v])
    visited = [False] * (n+1)
    visited[v] = True
    cnt = 1
    while q:
        v = q.popleft()
        for e in adj[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
                cnt += 1
    
    return cnt


n, m = map(int, input().split(' '))

adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)
tmp = -1
result = []

for _ in range(m):
    x,y = map(int, input().split(' '))
    adj[y].append(x)


for i in range(1, n+1):
    c = bfs(i)

    visited = [False] * (n+1)
    if c > tmp:
        result = [i]
        tmp = c
    elif c == tmp:
        result.append(i)

for i in result:
    print(i, end=' ')