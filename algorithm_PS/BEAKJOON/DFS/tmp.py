import sys
sys.setrecursionlimit(10**6) 

dd = [(1,0), (-1,0), (0,1), (0,-1)]


def check(array):
    for i in range(n):
        for j in range(m):
            if array[i][j] != 0:
                return True
    
    return False

def dfs(x,y):
    visited[x][y] = True

    for a,b in dd:
        dx = x+a
        dy = y+b

        if (0>dx or n<=dx or 0>dy or m<=dy):
            continue
        if visited[dx][dy] or array[dx][dy] < 0:
            continue
        dfs(dx,dy)


n,m = map(int, input().split(' '))
array = [[] for _ in range(n)]
visited = [[False] * m for _ in range(n)]
save_cnt = [[0]*m for _ in range(n)]

age = 0
cnt = 0

for i in range(n):
    array[i] = list(map(int, input().split(' ')))


while cnt < 2:
    cnt = 0
    age += 1

    for i in range(n):
        for j in range(m):
            if array[i][j] > 0:
                for x,y in dd:
                    dx = i+x
                    dy = j+y
                    if array[dx][dy] == 0:
                        save_cnt[i][j] += 1
    
    for i in range(n):
        for j in range(m):
            if array[i][j] >= save_cnt[i][j]:
                array[i][j] -= save_cnt[i][j]
            else:
                array[i][j] = 0
            
            save_cnt[i][j] = 0

                    
    for i in range(n):
        for j in range(m):
            if not(visited[i][j]) and array[i][j] != 0:
                dfs(i,j)
                cnt += 1
                visited = [[False] * m for _ in range(n)]

    for i in range(n):
        print(array[i])

                

    if not(check(array)):
        age = 0
        break
        

print(age)