def dfs(start, adj, visited):
    visited[start] = True

    for i in adj[start]:
        if not(visited[i]):
            dfs(i, adj, visited)

    return visited

def solution(n, computers):
    adj = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    cnt = 0

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                adj[i+1].append(j+1)
    

    for i in range(1, n+1):
        if not(visited[i]):
            visited = dfs(i, adj, visited)
            cnt+=1

    return cnt


# computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(3,computers))