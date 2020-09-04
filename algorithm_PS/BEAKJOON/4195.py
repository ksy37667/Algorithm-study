def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        count[x] += count[y]


test_case = int(input())

for _ in range(test_case):
    F = int(input())

    parent = dict()
    count = dict()

    for _ in range(F):
        x, y = input().split(' ')

        if x not in parent:
            parent[x] = x
            count[x] = 1
        if y not in parent:
            parent[y] = y
            count[y] = 1
        
        union(x,y)
    
        print(count[find(x)])
