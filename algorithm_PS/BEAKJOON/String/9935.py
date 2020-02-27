# https://www.acmicpc.net/problem/9935

N = list(input())
M = list(input())

result = []

for i in N:
    result.append(i)
    if M[-1] == i:
        if M == result[len(result)-len(M):]:
            for _ in range(len(M)):
                result.pop()


if len(result) == 0:
    print('FRULA')
else:
    for i in result:
        print(i, end='')