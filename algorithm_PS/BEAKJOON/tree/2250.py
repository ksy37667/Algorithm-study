# https://www.acmicpc.net/problem/2250

class Node:
    def __init__(self, value, left, right):
        self.parent = -1
        self.value = value
        self.left = left
        self.right = right


N = int(input())
root = -1
tree = {}
level_depth = 1

for i in range(1, N+1):
    tree[i] = Node(i, -1, -1)


for _ in range(N):
    value, left, right = map(int, input().split())
    tree[value].left = left
    tree[value].right = right
    
    if left != -1:
        tree[left].parent = value
    if right != -1:
        tree[right].parent = value

for i in range(1, N+1):
    if tree[i].parent == -1:
        root = i

save = [[] for _ in range(N+1)]



cnt = 1
def inorder(node, dept):
    global cnt, level_depth
    level_depth = max(level_depth, dept)
    if node.left != -1:
        inorder(tree[node.left], dept+1)
    save[dept].append(cnt)
    cnt += 1
    if node.right != -1:
        inorder(tree[node.right], dept+1)



inorder(tree[root], 1)

tmp =  max(save[1]) - min(save[1]) + 1
result = 1

for i in range(2, level_depth+1):
    if tmp < max(save[i]) - min(save[i]) + 1:
        result = i
        tmp = max(save[i]) - min(save[i]) + 1        

print(result, tmp)