n = int(input())
array = []
# 1 1 2 3 5
#   1 1 1

for _ in range(n):
    array.append(int(input()))
array = sorted(array)

result = 0
for i in range(1, len(array)+1):
    result += abs(i - array[i-1])

print(result)