from collections import deque


def dfs():
    pass

maxList = []
M = int(input())
arr = [0 for _ in range(M)]
for i in range(M):
    arr[i] = list(map(int, input().split(' ')))
    maxList.append(max(arr[i]))

maxValue = max(maxList)

