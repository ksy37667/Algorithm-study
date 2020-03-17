def check(p):
    cnt = 0
    
    for i in p:
        if i == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True

def recursion(p):
    left = 0
    right = 0
    u = ''
    v = ''
    
    for i in p:
        if i == '(':
            left += 1
        else:
            right += 1
        
        if left == right:
            u = p[0:left+right]
            v = p[left+right:]
    

def solution(p):
    if check(p):
        return p
    return recursion(p)
