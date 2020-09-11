import heapq

def solution(operations):
    queue = []
    answer = []

    for i in operations:
        commend, value = i.split(' ')
        if commend == 'D':
            if not(queue):
                continue
            if value == '1':
                data = max(queue)
                queue.pop(queue.index(data))
            else:
                heapq.heappop(queue)
        else:
            heapq.heappush(queue, int(value))

    if queue:
        answer = [max(queue), heapq.heappop(queue)]
    else:
        answer = [0,0]
    return answer

queue = ["I 16","D 1"]

queue = ["I 7","I 5","I -5","D -1"]

# queue = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]

print(solution(queue))