from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

visited = []

def bfs(arr ,start,n):
    visited[start[0]][start[1]] = True
    queue = deque()
    queue.append(start)

    while queue:
        start = queue.popleft()

        for i in range(4):
            x = start[0] + dx[i]
            y = start[1] + dy[i]
            
            if x >= 0 and y >= 0 and x < len(arr) and y < len(arr):
                if visited[x][y] == False and arr[x][y] == n:
                    queue.append([x,y])
                    visited[x][y] = True          
        


def solutiuon(v):
    answer = [0] * 3

    for i in range(len(v)):
        visited.append([False]* len(v))
    
    for i in range(len(v)):
        for j in range(len(v)):
            if visited[i][j] == False:
                bfs(v,(i,j), v[i][j])
                answer[v[i][j]] += 1

    return answer


# print(solutiuon([[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]))
print(solutiuon([[0,0,1],[2,2,1],[0,0,0]]))