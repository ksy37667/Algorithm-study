# https://www.acmicpc.net/problem/1543


str1 = input()
str2 = input()
cnt = 0
index = 0

while len(str2) <= len(str1) - index:
    if str1.startswith(str2, index, len(str1)):
        index += len(str2)
        cnt += 1
    else:
        index += 1

print(cnt)