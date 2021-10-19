#二维列表的创建
    #method 1
import random
list = []

for i in range(0,10):
    list.append([])
    for j in range(0,2):
        list[i].append(random.randint(-100,100))
print(list)

    #method 2

list2 = [[random.randint(-100,100) for j in range(2)] for i in range(10)]
print(list2)
