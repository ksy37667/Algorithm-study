import math

# def find(x):
#     if x == parent[x]:
#         return x
#     else:
#         p = find(parent[x])
#         parent[x] = p
#         return parent[x]

# def union(x,y):
#     x = find(x)
#     y = find(y)

#     if x != y:
#         parent[y] = x

def find(node):
    # path compression
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union-by-rank 기법
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2

        if rank[root1] == rank[root2]:
            rank[root2] += 1 


test_case = int(input())

for _ in range(test_case):
    N = int(input())
    array = []
    parent = dict()
    rank = dict()

    for i in range(N):
        array.append(list(map(int, input().split(' '))))
        parent[i] = i
        rank[i] = 0
        
    
    cnt = N
    for i in range(N-1):
        for j in range(i+1, N):
            if pow(array[i][0] - array[j][0],2) + pow(array[i][1] - array[j][1],2) <= pow(array[i][2] + array[j][2],2):
                union(i,j)
                cnt -= 1

    
    print(cnt)
