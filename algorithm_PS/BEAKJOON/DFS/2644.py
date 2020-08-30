def dfs(graph, x, visited, cnt):
    visited[x] = True

    for i in graph[x]:
        if not visited[i]:
            # print(i)
            count[i] = cnt
            dfs(graph, i, visited, cnt+1)

n = int(input())
x, y = map(int, input().split(' '))
m = int(input())

visited = [False] * (n+1)
graph = [[] for i in range(n+1)]
count = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)
    
dfs(graph, x, visited, 1)

if count[y] == 0:
    print(-1)
else:
    print(count[y])