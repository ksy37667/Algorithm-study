# https://www.acmicpc.net/problem/1715
import heapq

N = int(input())

queue = []

for _ in range(N):
    x = int(input())
    heapq.heappush(queue, x)

result = 0

while len(queue) > 1:
    one = heapq.heappop(queue)
    two = heapq.heappop(queue)
    sum_value = one + two
    result += sum_value
    heapq.heappush(queue, sum_value)

print(result)