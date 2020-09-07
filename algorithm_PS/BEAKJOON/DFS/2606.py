def dfs(v):
    global cnt
    cnt += 1
    visited[v] = True

    for i in adj[v]:
        if not(visited[i]):
            dfs(i)


n = int(input())
m = int(input())

adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for i in range(m):
    x,y = map(int, input().split(' '))

    adj[x].append(y)
    adj[y].append(x)

dfs(1)

print(cnt-1)