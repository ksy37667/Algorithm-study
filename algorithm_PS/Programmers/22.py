def solution(office, k):
    count = 0
    save = 0

    for i in range(len(office)-k+1):
        for j in range(len(office)-k+1):
            for m in range(i, k+i):
                for l in range(j, k+j):
                    if office[m][l] == 1:
                        count += 1
            if save < count:
                save = count
            count = 0
            
    return save


print(solution([[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,1,0]], 2))


