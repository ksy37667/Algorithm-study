from sys import stdin

k = int(stdin.readline())

array = []

for _ in range(k):
    data = int(stdin.readline())
    
    if data == 0:
        if array:
            array.pop()
        continue
    
    array.append(data)

print(sum(array))