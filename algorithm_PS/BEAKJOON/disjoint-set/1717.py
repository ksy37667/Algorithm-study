n, m = map(int, input().split(' '))

example = dict()
rank = dict()

def find(num):
    if example[num] != num:
        example[num] = find(example[num])
    return example[num]

def union(num1, num2):
    root1 = find(num1)
    root2 = find(num2)

    if rank[root1] > rank[root2]:
        example[root2] = root1
    else:
        example[root1] = root2

        if rank[root1] == rank[root2]:
            rank[root2] += 1

for i in range(n+1):
    example[i] = i
    rank[i] = 0

for _ in range(m):
    c,a,b = map(int, input().split(' '))
    
    if c == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')

