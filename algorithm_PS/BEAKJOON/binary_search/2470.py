from sys import stdin

n = int(stdin.readline())
array = list(map(int, stdin.readline().split()))

array.sort()

a = 0
b = n-1
answer = float('inf')

res1 = a
res2 = b
while a < b:
    tmp = array[a] + array[b]
    if answer > abs(tmp):
        answer = abs(tmp)
        res1 = a
        res2 = b
    
    if abs(array[a] + array[b]) > abs(array[a+1] + array[b]):
        a += 1
    elif abs(array[a] + array[b]) > abs(array[a] + array[b-1]):
        b -= 1
    else:
        b -= 1


print(array[res1], array[res2])
    