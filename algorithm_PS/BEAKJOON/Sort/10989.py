import sys

n = int(sys.stdin.readline())

array = [0] * 10001

for i in range(n):
    data =  int(sys.stdin.readline())
    array[data] += 1


for idx, data in enumerate(array):
    for i in range(data):
        print(idx)