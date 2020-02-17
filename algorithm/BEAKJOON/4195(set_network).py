def find(x): # 최상위 parent를 찾는 함수
    if x == parent[x]:
        return x
    
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x,y): # 최상위 parent를 찾고 네트워크 숫자를 합치는 함수.
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        network[x] += network[y]
    # print(network[x])
    


N = int(input())

for i in range(N):
    parent = dict()
    network = dict()

    F = int(input())

    for _ in range(F):
        x, y = input().split(' ')

        if x not in parent:
            parent[x] = x
            network[x] = 1
        if y not in parent:
            parent[y] = y
            network[y] = 1
        union(x,y)
        print(network[find(x)])