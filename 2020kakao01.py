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
    if p == '':
        return p
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
            break
    if check(u) == True:
        return u + recursion(v)
    else:
        tmp = '('
        tmp += recursion(v) + ')'
        u = u[1:len(u)-1]
        for i in range(0,len(u)):
            if u[i] == '(':
                tmp += ')'
            else:
                tmp += '('

        return tmp
    

def solution(p):
    if check(p) == True:
        return p
    return recursion(p)



p = '12345'

print(p[0:-1])