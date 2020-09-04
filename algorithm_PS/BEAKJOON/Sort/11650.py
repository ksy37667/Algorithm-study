array = []

n = int(input())

for _ in range(n):
    array.append(tuple(map(int, input().split(' '))))


array = sorted(array)


for i in array:
    print(i[0], i[1])