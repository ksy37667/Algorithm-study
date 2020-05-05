def check(str1, str2):
    if len(str1) != len(str2):
        return False
    
    for i in range(0, len(str2)):
        if str2[i] == '?':
            continue
        elif str1[i] != str2[i]:
            return False
    
    return True

def solution(words, queries):
    answer = []
    cnt = 0
    for i in queries:
        for j in words:
            if check(j,i) == True:
                print(cnt)
        answer.append(cnt)
        cnt = 0

    return answer
