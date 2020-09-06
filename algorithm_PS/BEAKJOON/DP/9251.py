A = input()
B = input()


cache = [[0] * (len(B) + 1) for _ in range(len(A)+ 1)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            cache[i][j] = cache[i-1][j-1] + 1
        else:
            cache[i][j] = max(cache[i][j-1], cache[i-1][j])

print(cache[len(A)][len(B)])