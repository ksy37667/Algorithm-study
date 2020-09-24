import sys
from math import *
input = sys.stdin.readline

def initMin(start, end, node):
    if start == end:
        treeMin[node] = array[start]
        return treeMin[node]

    
    mid = (start + end) // 2
    treeMin[node] = min(initMin(start, mid, node * 2), initMin(mid + 1, end, node * 2 + 1))
    return treeMin[node]


def subMin(start, end, node, left, right):
    if left > end or right < start:
        return 1000000001
    
    if left <= start and end <= right:
        return treeMin[node]
    
    mid = (start+end) // 2
    return min(subMin(start, mid, node*2, left, right),subMin(mid + 1, end, node*2+1, left, right))



    
N, M = map(int, input().rstrip().split())

h = int(ceil(log2(N)))
t_size = 1 << (h+1)

treeMin = [0] * t_size
array = []

for i in range(N):
    array.append(int(input().rstrip()))

initMin(0,N-1, 1)


for _ in range(M):
    a, b = map(int,  input().rstrip().split())

    print(subMin(0, N-1, 1, a-1, b-1))
