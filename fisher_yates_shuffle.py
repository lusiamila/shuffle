import random

def fisher_yates_shuffle(list_of_num):
    for i in range(len(list_of_num)-1,0,-1):
        j = random.randint(0,i)
        list_of_num[i],list_of_num[j] = list_of_num[j],list_of_num[i]
    return list_of_num

some_list = list(range(0,100))

fisher_yates_shuffle(some_list)
print(some_list)