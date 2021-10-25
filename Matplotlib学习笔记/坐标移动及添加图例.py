import matplotlib.pyplot as plit
import numpy as np
import random

#设置函数方程
x = np.linspace(-3,3,60)
y = x**3

#创建图片
plit.figure('X**3 Function')
#数据传递
plit.plot(x,y)
#设置轴标签

plit.xlabel('X')
plit.ylabel('y')

#获得目前存在的轴信息
ax = plit.gca() 
#轴边操作
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#设定确定的x,y轴
ax.yaxis.set_ticks_position('left') 
ax.xaxis.set_ticks_position('bottom')
#移动轴位置
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))  #注意输入元素，仅能提供一个数值

#增加图例
plit.figure('aim')

l1 = plit.plot(x,y,label='up')     #该元素为一个list
l2 = plit.plot(x,y,label='down')

plit.legend()   #显示曲线label
plit.legend(handles = [l1[0],l2[0]],labels = ['aaa','bbb'],loc = 'best') #强行改变标签标志值

#展示图片
plit.show()