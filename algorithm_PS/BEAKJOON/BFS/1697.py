from collections import deque

N, K = map(int, input().split(' '))

MAX = 100001
array = [0] * MAX

def bfs():
    q = deque([N])

    while q:
        now_pos = q.popleft()

        if now_pos == K:
            return array[now_pos]
        
        for next_pos in (now_pos-1, now_pos+1, now_pos*2):
            if 0 <= next_pos < MAX and not array[next_pos]:
                array[next_pos] = array[now_pos] + 1
                q.append(next_pos)

print(bfs())