
def dfs(v, i):
    visited[v] = True

    for w in adj[v]:
        if not(visited[w]):
            dfs(w, i)
        elif visited[w] and w == i:
            result.append(w)


n = int(input())
adj = [[] for i in range(n+1)]
for i in range(n):
    adj[i+1].append(int(input()))

result = []
for i in range(1, n+1):
    visited = [False] * (n+1)
    dfs(i, i)

l = len(result)
print(l)

for i in range(l):
    print(result[i])