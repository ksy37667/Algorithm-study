f = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 2,
    'E': 4,
    'F': 3,
    'G': 1,
    'H': 3,
    'I': 1,
    'J': 1,
    'K': 3,
    'L': 1,
    'M': 3,
    'N': 2,
    'O': 1,
    'P': 2,
    'Q': 2,
    'R': 2,
    'S': 1,
    'T': 2,
    'U': 1,
    'V': 1,
    'W': 1,
    'X': 2,
    'Y': 2,
    'Z': 1
}

N, M = map(int, input().split())
name_input = input().split()
name = [[], []]
for i in range(2):
    for c in name_input[i]:
        name[i].append(f[c])
p = [[], []]
cur = 0
while name[0] and name[1]:
    p[0].append(name[cur].pop(0))
    cur ^= 1
if name[0]:
    p[0] += name[0]
elif name[1]:
    p[0] += name[1]

cur = 0
while len(p[cur]) != 2:
    for i in range(len(p[cur])-1):
        p[cur^1].append((p[cur][i]+p[cur][i+1])%10)
    p[cur] = []
    cur ^= 1
print(int(str(p[cur][0])+str(p[cur][1])), end='%')