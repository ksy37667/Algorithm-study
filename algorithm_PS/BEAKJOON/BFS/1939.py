# https://www.acmicpc.net/problem/1939

N, M = map(int, input().split(' '))
island = [[] for _ in range(N+1)]

def BFS(weight):
    queue = list()
    queue.append(start)
    visited = [False] * (N+1)
    visited[start] = True

    while queue:
        cur_node = queue.pop(0)
        for y, cur_weight in island[cur_node]:
            if not visited[y] and cur_weight >= weight:
                queue.append(y)
                visited[y] = True
    
    return visited[end]
    


MIN = 100000000
MAX = 1

for _ in range(M):
    a,b,c = map(int, input().split(' '))
    island[a].append((b,c))
    island[b].append((a,c))
    MIN = min(MIN, c)
    MAX = max(MAX, c)

start, end = map(int, input().split(' '))


result = MIN

while MIN <= MAX:
    mid = (MIN + MAX) // 2
    if BFS(mid):
        result = mid
        MIN = mid + 1
    else:
        MAX = mid-1

print(result)