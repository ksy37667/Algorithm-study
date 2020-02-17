# https://www.acmicpc.net/problem/10989\
# 계수정렬


import sys

li = [0] * 10001

N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())
    li[num] += 1



for i in range (1, 10001):
    if li[i] != 0:
        for j in range(li[i]):
            print(i)