# https://www.acmicpc.net/problem/2110

N, M = map(int, input().split(' '))

array = list()

for i in range(N):
    array.append(int(input()))

array.sort()

start = array[1] - array[0]
end = array[-1] - array[0]
cnt = 1

while start <= end:
    mid = (start + end) // 2
    value = array[0]
    cnt = 1
    for i in range(1,len(array)):
        if array[i] - value >= mid:
            value = array[i]
            cnt += 1
        
    if cnt >= M:
        start = mid+1
        result = mid
    else:
        end = mid-1


print(result)