from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])

    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True




N, M, V = map(int, input().split(' '))
visited = [False] * (N+1)

graph = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

    graph[a].sort()
    graph[b].sort()

dfs(graph, V, visited)
visited = [False] * (N+1)

print()
bfs(graph, V, visited)

