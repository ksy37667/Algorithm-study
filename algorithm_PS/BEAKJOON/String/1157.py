string = input().upper()

li = []

for i in set(string):
    li.append(string.count(i))

idx = [i for i, x in enumerate(li) if x == max(li)]

print(idx)

if len(idx) > 1:
    print("?")
else:
    print(list(set(string))[li.index(max(li))])
