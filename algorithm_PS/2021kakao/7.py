


def solution(sales, links):
    array = [[] for i in range(len(sales)+1)]


    for i in links:
        array[i[0]].append((i[1],sales[i[1]-1]))
    
    print(array)


sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]


solution(sales, links)