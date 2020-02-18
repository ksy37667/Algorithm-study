# https://www.acmicpc.net/problem/1668

def func(array):
    now = array[0]
    cnt = 1
    for i in range(1, len(array)):
        if now < array[i]:
            now = array[i]
            cnt += 1
    return cnt


N = int(input())
array = []

for i in range(N):
    array.append(int(input()))

print(func(array))
array.reverse()
print(func(array))