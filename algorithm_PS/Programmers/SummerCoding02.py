from math import gcd

def solution(w,h):
    num = gcd(w,h)
    
    if num == 1:
        answer = (w*h)-(w+h-1)
    else:
        answer = (w*h)-(w+h-num)
        
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/62048