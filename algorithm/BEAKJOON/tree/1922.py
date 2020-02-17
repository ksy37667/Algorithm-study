# 모든 간선 가중치 낮은 순서대로 sorting
# 사이클이 생기지 않는 조건을 생각하며 연결한다.

N = int(input())
M = int(input())

mygraph = {
    'vetices' : [i for i in range(1,N+1)],
    'edges':[]
}

for i in range(M):
    a, b, c = map(int, input().split(' '))
    mygraph['edges'].append((c,a,b))
    mygraph['edges'].append((c,b,a))



parent = dict()
rank = dict()

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


def make_set(node):
    parent[node] = node
    rank[node] = 0


def kruskal(graph):
    mst = list()
    total = 0
    # 초기화
    for node in graph['vetices']:
        make_set(node)

    # 2. weight 기반 sorting
    edges = graph['edges']
    edges.sort()

    # 3. 간선 연결(사이클 없는)
    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            total += edge[0]


    return total



print(kruskal(mygraph))
