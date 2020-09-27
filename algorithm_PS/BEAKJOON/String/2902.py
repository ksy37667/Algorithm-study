from sys import stdin

string = list(stdin.readline())
array = []

array.append(string[0])

for i in range(1, len(string)):
    if string[i] == '-':
        array.append(string[i+1])


for i in array:
    print(i, end='')