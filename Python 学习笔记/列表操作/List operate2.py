#列表随机数生成
    #method 1:
import random

List_num = []
for i in range(10):
    List_num.append(random.randint(-100, 100))
print(List_num)

    #method 2:
import random

List = [random.randint(-100,100) for i in range(10)]
print(List)

#列表计算
    #method 1:
List2 = [x*3 for x in List]
print(List2)

    #method 2:
List3 = []
for i in List:
    List3.append(i*3)
print(List3)

#新列表生成
List4 = [x for x in List if x > 30]
print('原列表：'+str(List))
print('筛选列表：'+str(List4))

