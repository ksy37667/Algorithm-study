import sys

sys.setrecursionlimit(1000000)

G = int(input())
P = int(input())
gate = {i:i for i in range(G+1)}
plane = []

for _ in range(P):
    plane.append(int(sys.stdin.readline()))

def find(num):
    if gate[num] == num:
        return num
    gate[num] = find(gate[num])
    return gate[num]

def union(x,y):
    x = find(x)
    y = find(y)
    gate[x] = y


cnt = 0

for i in plane:
    tmp = find(i)
    if tmp == 0:
        break

    union(tmp, tmp-1)
    print(gate)
    cnt += 1

print(cnt)