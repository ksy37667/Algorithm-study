from itertools import combinations, chain

def getSubset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s) + 1))

def getUniqueSubset(relation):
    subset_list = getSubset(list(range(0, len(relation[0]))))
    unique_list = []

    for subset in subset_list:
        unique = True
        check = set()
        for i in range(len(relation)):
            row = ' '
            for j in subset:
                row += relation[i][j] + '.'
            if row in check:
                unique = False
                break
            check.add(row)
        if unique:
            unique_list.append(subset)
    return unique_list


def solution(relation):
    unique_list = getUniqueSubset(relation)
    unique_list = sorted(unique_list, key=lambda x: len(x))

    answer_list = []

    for subset in unique_list:
        subset = set(subset)
        check = True
        for j in answer_list:
            if j.issubset(subset):
                check = False
        if check == True:
            answer_list.append(subset)
    return len(answer_list)

relation = [["100","ryan","music","2"]
    ,["200","apeach","math","2"]
    ,["300","tube","computer","3"]
    ,["400","con","computer","4"]
    ,["500","muzi","music","3"]
    ,["600","apeach","music","2"]
]

print(solution(relation))