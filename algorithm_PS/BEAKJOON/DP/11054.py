N = int(input())
array = list(map(int, input().split(' ')))

cache = [0 for i in range(N)]

cache[0] = 1
cache[1] = 2

for i in range(N):
