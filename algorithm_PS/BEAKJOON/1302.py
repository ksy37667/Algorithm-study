# https://www.acmicpc.net/problem/1302

dic = {}

N = int(input())

for i in range(N):
    book = input()
    if book in dic.keys():
        dic[book] += 1
    else:
        dic[book] = 1

array = []
target = max(dic.values())

for book, count in dic.items():
    if count == target:
        array.append(book)

print(sorted(array)[0])