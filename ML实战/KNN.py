import csv
import random
import math

#数据读取
with open('Prostate_Cancer.csv', 'r') as file:
    reader = csv.DictReader(file)
    dates = [row for row in reader]



#分组
random.shuffle(dates)
n = len(dates)//5
test_set = dates[0:n]
train_set = dates[n:]


#KNN   距离运算
def distance(d1, d2):
    sum_n = 0
    for key in ('radius', 'texture', 'perimeter', 'area', 'smoothness', 'compactness', 'symmetry', 'fractal_dimension'):
        sum_n += (float(d1[key])-float(d2[key]))**2
    return sum_n**0.5


k = 6   #取K的值,为范围内数据的数量


#距离获取 排序 取前k个 加权平均
def knn(data):
    res = [{"result": train['diagnosis_result'], "distance":distance(data, train)}
           for train in train_set]
    res_o = sorted(res, key= lambda x: x['distance'], reverse=False)

    res_k = res_o[:k]

    #print(res_k)

    #加权平均
    result = {'B': 0, 'M': 0}
    # 距离总和
    sum = 0

    for dis in res_k:
        sum += dis['distance']

    for w in res_k:
        result[w['result']] += 1-w['distance']/sum

    print(result)

    print(data['diagnosis_result'])

    if result['B'] > result['M']:
        return 'B'
    else:
        return 'M'


#总次数记录   单次训练结果

"""
finnal_test = knn(test_set[0])

correct = 0
uncorrect = 0


if finnal_test == test_set[0]['diagnosis_result']:
    correct += 1
else :
    uncorrect += 1

print('正确率=',correct/(correct+uncorrect))
"""

#完整测试集训练 全部训练结果
correct = 0
uncorrect = 0
print('训练开始')

for i in range(n):
    finnal_test = knn(test_set[i])
    print('第{}次训练，共{}次'.format(i,n))
    if finnal_test == test_set[i]['diagnosis_result']:
        correct += 1
    else:
        uncorrect += 1

print('正确率={:.2f}%'.format((correct/(correct+uncorrect))*100))



