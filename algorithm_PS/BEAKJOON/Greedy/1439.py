S = input()
cnt = 0

if S[0] =='1':
    trigger = True
    for i in range(len(S)):
        if trigger:
            if S[i] == '0':
                cnt+=1
                trigger = False
        else:
            if S[i] == '1':
                trigger = True
else:
    trigger = True
    for i in range(len(S)):
        if trigger:
            if S[i] == '1':
                cnt+=1
                trigger = False
        else:
            if S[i] == '0':
                trigger = True

print(cnt)