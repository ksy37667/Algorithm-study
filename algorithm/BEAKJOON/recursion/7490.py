# https://www.acmicpc.net/problem/7490

import copy

def recursion(array, n):
    if len(array) == n:
        save_array.append(copy.deepcopy(array))
        return
    
    for i in sign:
        array.append(i)
        recursion(array,n)
        array.pop()


    

test_case = int(input())

sign = [' ', '+', '-']

for _ in range(test_case):
    N = int(input())
    save_array = []

    recursion([], N-1)
    number = [i for i in range(1,N+1)]

    for i in save_array:
        string = ""
        for j in range(N-1):
            string += str(number[j]) + i[j]
        string += str(number[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
    
    print()
