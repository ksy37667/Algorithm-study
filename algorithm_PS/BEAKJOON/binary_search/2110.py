# https://www.acmicpc.net/problem/2110

N, M = map(int, input().split(' '))
array = []

for _ in range(N):
    array.append(int(input()))

array = sorted(array)

start = array[1] - array[0]
end = array[-1] - array[0]
result = 0

while (start <= end):
    mid = (start + end) // 2
    cnt = 1
    save = array[0]
    
    for i in range(1, len(array)):
        if array[i] - save >= mid:
            cnt += 1
            save = array[i]
    
    if cnt >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1


print(result)