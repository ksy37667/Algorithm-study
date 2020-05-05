def solution(n):
    answer = [0,0,1,0,0,1,1]
    
    if n == 1:
        return [0]
    elif n == 2:
        return [0,0,1]
    elif n == 3:
        return [0,0,1,0,0,1,1]
    else:
        for i in range(3,n):
            answer= answer[:len(answer)//2]+[0]+answer[len(answer)//2+1:]+[0]+answer[:len(answer)//2]+[1]+answer[len(answer)//2+1:]
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/62049