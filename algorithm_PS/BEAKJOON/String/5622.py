string = input()

dic = {
    1 : '', 
    2 : 'ABC',
    3 : 'DEF',
    4 : 'GHI',
    5 : 'JKL',
    6 : 'MNO',
    7 : 'PQRS',
    8 : 'TUV',
    9 : 'WXYZ'
}

result = 0

for i in string:
    for key, value in dic.items():
        if i in value:
            result += key


print(result + len(string)) 