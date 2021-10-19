#维度变换
import torch


a = torch.rand(4, 1, 28, 28)
print(a.shape)

# print(a.view(4, 28*28))      # 将末尾三个部分整合到一起  ，类似一个reshape函数，将原张量重新拼接。

#数据的理解方式：
print(a.view(4*28, 28).shape)    # torch.Size([112, 28])       将行合并到一起，只关注一行的数据。
print(a.view(4, 28*28).shape)     # torch.Size([4, 784])       只关心通道的数据
print(a.view(4, 1, 28, 28).shape)    # torch.Size([4, 1, 28, 28])
