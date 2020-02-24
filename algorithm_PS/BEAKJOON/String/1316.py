test = int(input())


result = 0

for _ in range(test):
    string = list(input())
    li = []
    result += 1
    for i in range(0,len(string)):
        if i == 0:
            li.append(string[i])
        elif string[i-1] == string[i]:
            continue
        elif string[i] in li:
            result -= 1
            break
        else:
            li.append(string[i])

    
print(result)