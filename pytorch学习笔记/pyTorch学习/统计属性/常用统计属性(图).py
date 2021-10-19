import torch

a = torch.arange(1,9).view(2,4).float()

print(a)

print(a.max(),a.min(),a.mean(),a.prod(),a.sum(),a.argmax(),a.argmin())
#将所有维度打平操作。  mean均值平均，prod累乘，argmax最大值索引


#处理不同维度的最大值
b = torch.rand(2,3,4)
print(b)

"""b tensor 样例
tensor([[[0.5633, 0.6880, 0.2160, 0.8232],
         [0.5042, 0.0384, 0.8538, 0.9720],
         [0.6416, 0.0484, 0.9541, 0.4876]],

        [[0.0921, 0.4564, 0.1316, 0.3578],
         [0.6068, 0.1735, 0.9936, 0.8516],
         [0.6473, 0.7560, 0.3782, 0.1479]]])
[2,3,4]
"""
print(b.argmax())   #打平操作

print(b.argmax(dim=0))
print(b.argmax(dim=1))
print(b.argmax(dim=2))

#消掉dim维度，在剩下矩阵中求最大值，最小值同理。
