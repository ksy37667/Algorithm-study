# 모든 간선 가중치 낮은 순서대로 sorting
# 사이클이 생기지 않는 조건을 생각하며 연결한다.

mygraph = {
    'vetices' : ['A','B','C','D','E','F','G'],
    'edges':[
        (7,'A','B'),
        (5,'A','D'),
        (7,'B','A'),
        (8,'B','C'),
        (9,'B','C'),
        (7,'B','E'),
        (8,'C','B'),
        (5,'C','E'),
        (5,'D','A'),
        (9,'D','B'),
        (7,'D','E'),
        (6,'D','F'),
        (7,'E','B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}


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
            mst.append(edge)


    return mst

print(kruskal(mygraph))