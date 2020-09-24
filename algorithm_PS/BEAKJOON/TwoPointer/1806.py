n, m = map(int, input().split())
array = list(map(int, input().split()))


cache = [0] * (n+1)
for i in range(1, n+1):
    cache[i] = cache[i-1] + array[i-1]



answer = 1000001
start = 0
end = 1

while start != n:
    if cache[end] - cache[start] >= m:
        if end - start < answer:
            answer = end-start
        start += 1
    
    else:
        if end != n:
            end += 1
        else:
            start += 1
    

if answer != 1000001:
    print(answer)
else:
    print(0)


