# https://www.acmicpc.net/problem/11650

N = int(input())

array = []
for i in range(N):
    input_data = input().split(' ')
    array.append((int(input_data[0]), int(input_data[1])))


array.sort()

for i in array:
    print(i[0], i[1])