# import sys
# import math
# n, k = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))

# answer = math.inf
# start_idx = arr.index(min(arr))
# for i in range(k):
# 	cnt = 1
# 	front, back = arr[:start_idx-i], arr[start_idx+k-i:]
# 	front_cnt = len(front) // (k-1) + (1 if len(front) % (k-1) else 0)
# 	back_cnt = len(back) // (k-1) + (1 if len(back) % (k-1) else 0)
# 	answer = min(answer, cnt + front_cnt + back_cnt)
# print(answer)



# test_case = int(input())

# for _ in range(test_case):
#     answer = 0

#     n, m = map(int, input().split(' '))

#     k1 = n/5

#     k2 = (n+m)/12

#     k = k1 if k1 < k2 else k2

#     while n+m < 12*k:
#         if k == 0:
#             break
#         k -= 1

#     print(k)




# import sys

# n = int(input())
# time = []

# for i in range(n):
#     time.append(list(input().split(" ~ ")))

#     for j in range(len(time[i])):
#         time[i][j] = int(time[i][j].replace(":", ""))

    
# stData = 0
# endData = sys.maxsize

# for data in time:
#     if data[0] > stData:
#         stData = data[0]
    
#     if data[1] < endData:
#         endData = data[1]

# if endData <= stData:
#     print(-1)
# else:
#     stData = str(stData)
#     endData = str(endData)

#     if len(stData) == 3:
#         stData = "0" + stData[0:]
#     if len(endData) == 3:
#         endData = "0" + stData[0:]

#     if len(stData) == 2:
#         stData = "00" + stData[0:]
#     if len(endData) == 2:
#         endData = "00" + stData[0:]

#     if len(stData) == 1:
#         stData = "000" + stData[0:]
#     if len(endData) == 1:
#         endData = "000" + stData[0:]

#     stData = stData[0:2] + ":" + stData[2:]
#     endData = endData[0:2] + ":" + endData[2:]

#     print(stData, "~", endData)




# n = int(input())

# arr = [[] for _ in range(n)]
# size = [0] * (n+1)
# direction = []

# for i in range(n):
#     arr[i] = list(str(input()))


# for i in range(n):
#     for j in range(n):
#         if arr[i][j] == '1':
#             direction.append((i,j))
#             size[1] += 1



# for data in range(1, n):

#     for dd in direction:
#         check = 0
#         for i in range(data-1, data):
#             for j in range(data-1, data):
#                 try:
#                     if arr[dd[0] + i][dd[1] + j] == 0:
#                         check = 1
#                         break
#                 except IndexError:
#                     continue
            
#             if check == 1:
#                 break

#         if check == 0:
#             size[data] += 1


# print(size[1])
# print(direction)


# score = list(map(float, input().split(' ')))

# n, m = map(int, input().split(' '))
# info = []
# content = []
# Ylist = []
# Olist = []
# # print(ord('A'))

# for i in range(n):
#     info.append(list(str(input())))

# for i in range(n):
#     content.append(list(str(input())))


# for i in range(n):
#     for j in range(m):
#         if info[i][j] == 'Y':
#             Ylist.append((content[i][j], score[ord(content[i][j])-65],i,j))
#         elif info[i][j] == 'O':
#             Olist.append((content[i][j], score[ord(content[i][j])-65],i,j))

# Ylist = sorted(Ylist, key=lambda x: (x[2], x[3]))
# Olist = sorted(Olist, key=lambda x: (x[2], x[3]))

# Ylist = sorted(Ylist, key=lambda x: x[1], reverse=True)
# Olist = sorted(Olist, key=lambda x: x[1], reverse=True)



# for data in Ylist:
#     print(data[0], data[1], data[2], data[3])

# for data in Olist:
#     print(data[0], data[1], data[2], data[3])


# LI = [(1,3), (1,2), (2,3), (2,1), (3,1)]

# print(sorted(LI, key=lambda x: (x[0], x[1])))

# B 4.3 0 1
# D 4.3 1 0
# C 2.1 1 1
# E 5.0 1 2
# C 2.1 0 2



# from collections import deque
# import sys



# def bfs(arr, visited, start, count):
#     visited[start[0]][start[1]] = True
#     queue = deque()
#     queue.append([start[0],start[1],0])

#     while queue:
#         start = queue.popleft()

#         for i in range(3):
#             x = start[0] + dx[i]
#             y = start[1] + dy[i]
#             print(x,y)
            
#             if x >= 0 and y >= 0 and x < N and y < M:
#                 if visited[x][y] == False and arr[x][y] == '.':
#                     if (i == 1 or i == 2) and x != N-1:
#                         queue.append([x,y])
#                         visited[x][y] = True
#                         count[x][y] = count[start[0]][start[1]] + 1    
#                     elif x != N-1:
#                         queue.append([x,y])
#                         visited[x][y] = True
#                         count[x][y] = count[start[0]][start[1]]


# def dijkstra(start, array, visit):
#     dx = [0,0,-1,1]
#     dy = [-1,1,0,0]
#     queue = []
#     heapq.heappush(queue,start)

#     while queue:
#         dist, x, y = heapq.heappop(queue)
#         visit[x][y] = 1

#         if x == N-1 and y == M-1:
#             return dist

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
#                 visit[nx][ny] = 1
#                 if array[nx][ny] == "0":
#                     heapq.heappush(queue, [dist,nx,ny])
#                 elif array[nx][ny] == "1":
#                     heapq.heappush(queue, [dist+1,nx,ny])





















# import heapq

# M, N = map(int, input().split(' '))

# array = []

# for i in range(N):
#     array.append(list(input()))

# visit = [[0 for _ in range(M)] for _ in range(N)]

# def dijkstra(start, array, visit,end):
#     dx = [0,0,1]
#     dy = [-1,1,0]
#     visit = [[0 for _ in range(M)] for _ in range(N)]
#     queue = []
#     heapq.heappush(queue,start)

#     while queue:
#         dist, x, y = heapq.heappop(queue)
#         visit[x][y] = 1

#         if x == end[0] and y == end[1]:
#             return dist

#         for i in range(3):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
#                 visit[nx][ny] = 1
#                 if array[nx][ny] == ".":
#                     if i == 0 or i == 1:
#                         heapq.heappush(queue, [dist+1,nx,ny])
#                     else:
#                         heapq.heappush(queue, [dist,nx,ny])
    
#     return -1

# result = []

# for i in range(M):
#     if array[0][i] == 'c':
#         for j in range(M):
#             if array[N-1][j] == '.':
#                 result.append(dijkstra([0,0,i],array,visit, [N-1,j]))

# if result: 
#     print(min(result))
# else:
#     print(-1)



# arr = []
# count = []
# visited = []
# result = sys.maxsize

# for i in range(N):
#     arr.append(list(str(input())))
#     visited.append([False]*M)
#     count.append([0]*M)


# for i in range(M):

#     if arr[0][i] == 'c':
#         bfs(arr, visited, [0,i], count)
    
#     for j in range(M):
#         if arr[N-1][j] == ".":
#             result = min(result, count[N-1][j])

# print(result)
# print(count)


















m, n = map(int, input().split(' '))

arr = []

dp = [[0 for i in range(m)]for i in range(n)]

for _ in range(n):
    arr.append(list(map(int, input().split(' '))))


for i in range(n):
    dp[i][0] = arr[i][0]

for i in range(m):
    dp[0][i] = arr[0][i]

print(dp)

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i][j-1] + arr[i][j], dp[i-1][j] + arr[i][j])

print(dp[n-1][m-1])