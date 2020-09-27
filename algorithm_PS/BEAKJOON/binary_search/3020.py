from sys import stdin

N, H = map(int, stdin.readline().split())

array = [0] * N

down = []
up = []

for i in range(N):
    input_list_2 = stdin.readline().split()
    input_num = int(input_list_2[0])
    if i % 2 == 0:
        
        up.append(input_num)
    else:
        down.append(input_num)


down.sort()
up.sort()
result = N
cnt = 0

