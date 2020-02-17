from random import *

rand_data_list = list()

for num in range(10):
    rand_data_list.append(randint(1,100))

print(rand_data_list)



def sequential(data_list, search_data):
    for index in range(len(data_list)):
        if data_list[index] == search_data:
            return index
        return -1


print(sequential(rand_data_list, 5))