from itertools import chain, combinations

def get_subset(num):
    result = []
    for i in range(2, len(num)+1):
        c = combinations(num,i)
        result.extend(c)

    return result

def solution(orders, course):
    save = []
    for i in orders:
        save.append(get_subset(i))

    cache = []

    # print(save[0])

    for i in course:
        for j in range(len(save)):
            for k in save[j]:
                cnt = 0
                if k in cache:
                    continue
                if i == len(k):
                    for l in range(j+1, len(save)):
                        for p in save[l]:
                            if p == k:
                                cnt+=1
                if cnt >= 1:
                    cache.append(k)
                
    print(cache)






orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,5]
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
solution(orders, course)
