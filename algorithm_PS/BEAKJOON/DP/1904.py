# https://www.acmicpc.net/problem/11054

N = int(input())
divnum = 15746

cache = [0 for i in range(N+1)]

cache[1] = 1
cache[2] = 2

for i in range(3,N+1):
    cache[i] = (cache[i-2] + cache[i-1])%15746

print(cache[-1])