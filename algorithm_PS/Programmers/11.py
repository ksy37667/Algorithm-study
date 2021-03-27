def solution(estimates, k):
    a = 0
    save = 0

    cache = sum(estimates[a:a+k])
    save = sum(estimates[a:a+k])

    for i in range(k,len(estimates)):
        if cache < save - estimates[a] + estimates[i]:
            cache = save - estimates[a] + estimates[i]
        
        save = save - estimates[a] + estimates[i]
        a += 1

    return cache



print(solution([10, 1, 10, 1, 1, 4, 3, 10], 6))