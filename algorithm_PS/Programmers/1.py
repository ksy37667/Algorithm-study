def solution(n, delivery):
    result = ['?'] * (n+1)

    # delivery.sort()

    for data in delivery:
        if data[2] == 1:
            result[data[0]] = 'O'
            result[data[1]] = 'O'
    
    for data in delivery:
        if data[2] == 0:
            if result[data[0]] == 'O':
                result[data[1]] = 'X'
            elif result[data[1]] == 'O':
                result[data[0]] = 'X'

    
    a = str()
    for i in range(1, len(result)):
        a += result[i]
    
    return a