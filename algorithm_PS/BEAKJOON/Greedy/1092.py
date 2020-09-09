import sys

n = int(input())
crane = sorted(list(map(int, input().split(' '))))
m = int(input())
weight = sorted(list(map(int, input().split(' '))))

cnt = 0

if weight[-1] > crane[-1]:
    print(-1)
    sys.exit()

while True:
    for i in crane:
        for j in range(len(weight)-1, -1, -1):
            if i>=weight[j]:
                del weight[j]
                break
    cnt += 1
    
    if not weight:
        print(cnt)
        break


