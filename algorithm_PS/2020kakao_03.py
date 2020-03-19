def rotation(key):
    N = 3
    ret = [[0] * 3 for _ in range(3)]

    for i in range(3):
        for j in range(3):
            ret[j][N-1-i] = m[i][j]
    
    return ret


def solution(key, lock):
    
    answer = True
    return answer

