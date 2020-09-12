def solution(info, query):
    array = [[] for _ in range(len(info))]
    condition = [[] for _ in range(len(query))]

    for i in range(len(info)):
        array[i] = list(info[i].split(' '))

    for i in range(len(query)):
        query[i] = query[i].replace('and ','')
        condition[i] = list(query[i].split(' '))

    answer = []

    for i in range(len(condition)):
        cnt = 0
        for j in range(len(array)):
            check = True
            for k in range(4):
                if condition[i][k] == '-':
                    continue
                elif condition[i][k] != array[j][k]:
                    check = False
                    break
            if int(array[j][4]) < int(condition[i][4]):
                check = False

            if check:
                cnt += 1
        answer.append(cnt)

    condition = sorted(condition)
    array = sorted(array)
    for i in condition:
        print(i)
    
    for i in array:
        print(i)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

solution(info, query)