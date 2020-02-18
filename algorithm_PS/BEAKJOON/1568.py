N = int(input())
cnt = 1
result = 0
while N != 0:
    if cnt > N:
        cnt = 1

    N -= cnt
    cnt += 1
    result += 1

print(result)

