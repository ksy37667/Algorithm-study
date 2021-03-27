# import sys    
# sys.setrecursionlimit(10000)

# array = [[] for i in range(301)]


# def recursion(k, count):
#     pass

def solution(n, k):
    # count = 1

    # for i in range(1,301):
    #     array[i].append(i)

    # for i in range(1,n+1):
    #     for j in range(1,k+1):
    #         recursion(j,count)

    count = 0

    array = [0] * (n+1)
    dp = [0] * (n+1)

    for i in range(1,n+1):
        array[i] = i

    for i in range(1, k):
        dp[i] = array[i]

        for j in range(1,i):
            if array[j] < array[i] and dp[i] < dp[j] + array[i]:
                dp[i] = dp[j] + array[i]
        
    print(dp)

    return count


print(solution(10,2))