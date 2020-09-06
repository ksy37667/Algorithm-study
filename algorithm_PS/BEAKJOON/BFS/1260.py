from collections import deque

def dfs(v):
    visited[v] = True
    print(v, end=' ')

    for i in array[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    q = deque([v])

    while q:
        v = q.popleft()
        if not(visited[v]):
            visited[v] = True
            print(v, end=' ')
            for i in array[v]:
                if not visited[i]:
                    q.append(i)

n, m, v = map(int, input().split(' '))

array = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split(' '))
    array[x].append(y)
    array[y].append(x)

for i in array:
    i.sort()

visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)