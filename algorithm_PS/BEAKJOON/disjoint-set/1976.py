N = int(input())
M = int(input())

graph = {i:i for i in range(1, N+1)}
rank = {i:0 for i in range(1, N+1)}

def find(num):
    if graph[num] != num:
        graph[num] = find(graph[num])
    return graph[num]

def union(num1, num2):
    root1 = find(num1)
    root2 = find(num2)

    if rank[root1] > rank[root2]:
        graph[root2] = root1
    else:
        graph[root1] = root2

        if graph[root1] == graph[root2]:
            rank[root2] += 1


for i in range(1,N+1):
    maps = list(map(int, input().split(' ')))
    for j in range(1, len(maps)+1):
        if maps[j-1] == 1:
            union(i,j)

li = list(map(int, input().split(' ')))
result = set([find(i) for i in li])

if len(result) != 1:
    print("NO")
else:
    print("YES")