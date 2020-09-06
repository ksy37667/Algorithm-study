from collections import deque

def bfs(c):
    queue = deque([st_node])

    visited = [False] * (n + 1)
    visited[st_node] = True

    while queue:
        data = queue.popleft()
        for y, weight in adj[data]:
            if not visited[y] and weight >= c:
                visited[y] = True
                queue.append(y)
    
    return visited[end_node]


n, m = map(int, input().split(' '))

adj = [[] for _ in range(n+1)]
start = 1000000000
end = 1

for _ in range(m):
    a,b,c = map(int, input().split(' '))
    adj[a].append((b,c))
    adj[b].append((a,c))
    start = min(start, c)
    end = max(end, c)


st_node, end_node = map(int, input().split(' '))


result = start

while(start <= end):
    mid = (start + end) // 2

    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1


print(result)