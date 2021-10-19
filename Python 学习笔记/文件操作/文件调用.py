import os

#file = open('g:\\nio.txt', 'a')    # 在文件后加如数据
#file.write('sweoipow')        写入数据

#file.close()

file = open('g:\\nio.txt', 'r', encoding='UTF-8')
number = 0
while True:
    number += 1
    line = file.readline()
    if line == '':
        break
    print(number, line)

