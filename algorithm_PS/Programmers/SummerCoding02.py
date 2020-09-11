from itertools import combinations

def solution(numbers):
    a = list(combinations(numbers, 2))
    answer = []
    for i in a:
        if not (i[0] + i[1])in answer:
            answer.append(i[0]+i[1])
    
    answer = sorted(answer)
    return answer



def solution(n):
    array = [[0]*n for i in range(n)]

    x, y = -1, 0

    num = 0

    for i in range(n):
        for j in range(i,n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            num += 1 
            array[x][y] = num
    answer = []

    for i in range(n):
        for j in range(i+1):
            answer.append(array[i][j])

    return answer

print(solution(5))


from itertools import combinations, permutations

check = 0
c = 0
def solve(k, combi, array):
    global check
    global c
    if k == len(combi):
        for i in range(len(array[0])):
            cnt = 0
            for j in range(len(array)):
                if array[j][i] == 1:
                    cnt+= 1
            if cnt%2:
                return
        check += 1
        return

    for i in combi[k]:
        array[k] = i
        solve(k+1, combi, array)


def solution(a):
    arr = [[0] * len(a) for _ in range(len(a[0]))]

    for i in range(len(a)):
        for j in range(len(a[0])):
            arr[j][i] = a[i][j]

    count = [0] * len(arr)
    array = [[] for _ in range(len(arr))]

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                count[i] += 1
    combi = [0] * len(arr)
    for i in range(len(count)):
        combi[i] = set(combinations(arr[i], len(arr[0])))
    
    print(combi)

    solve(0, combi, array)
    print(int(check%(10e7+19)))


m = [[1,0,0,1,1],[0,0,0,0,0],[1,1,0,0,0],[0,0,0,0,1]]
m = [[0,1,0],[1,1,1],[1,1,0],[0,1,1]]
# m = [[1,0,0],[1,0,0]]
solution(m)


# def solution(a):
#     cnt = 0
#     for i in range(len(a)):
#         for j in range(len(a)):
#             if i == j or i == j-1:
#                 continue
#             if len(a) == 1:
#                 cnt+= 1
#                 break

#             if a[j] > a[j-1]:
#                 a.remove(a[j])
#             else:
#                 a.remove(a[j-1])
    
#     print(cnt)

# a = [9,-1,-5]
# solution(a)