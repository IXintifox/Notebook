import torch
import numpy
from numpy import *

x = torch.rand(2, 2, 3, 3)
y = torch.randn(2, 2, 3, 3)

print(x, '\n\n', y)
'''
x 满足，取值范围为[0,1]
y 满足取值范围为正态分布
'''

a = array([2, 3.3])
print('array单列表数据的输出：',a.shape,'\n')
#转化为torch类型的数据
a = torch.from_numpy(a)
print('array数据转为tensor的数据类型的输出：',a.shape,'\n')
print('numpy转化数据的的直接输出：',a,'\n')


b = array([[2,3],[3,4]])    #numpy真实创建数据
print('array双列表数据输出',b.shape,'\n')
b = torch.from_numpy(b)
print('b双列表数据的输出',b.shape,'\n')      #torch类型为[2,2]
print('b的数据输出',b)


data,num = b
print('numpy转化数据的标签获取{},{}'.format(data,num))    #最后为标注信息，每组输出都会包含。

print('\n'*3,'* *'*30,"\n"*2)
#不同输出类型ones的比较

#非标准输入
a1 = torch.ones(2,2)
a1v = torch.ones([2,2])      #a1和 a1v的输入模式不同，输出结果相同。
a2 = numpy.ones([2,2])      #numpy类型的数据，创建一个列表，一共有两组，每组两个元素。
print('torch.one类型',a1,'\n','torch.one另一种输入类型',a1v,'\n','numpy类型',a2)
print('torch',type(a2))
a2 = torch.from_numpy(a2)
print(a2)
print(type(a1),type(a2))

#创建小数类型的tensor
a3 = torch.Tensor([2.1,1])    #固定张量数据   #大写的Tensor接受固定的维度或现有的数据，大写必须有list[]，小写的tensor接受现有的数据。
print(a3)
a4 = torch.FloatTensor([2.3, 1.2])
a5 = torch.FloatTensor([2.,1])    #不会提示类型
print(a4,'\n',a5)
a6 = torch.FloatTensor(2,3,4)
print(a6.shape)


