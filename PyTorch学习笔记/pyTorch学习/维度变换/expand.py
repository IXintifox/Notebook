import torch

#创建张量
a = torch.tensor([1, 2, 3])
b = torch.randn(2, 2, 3, 2)
c = torch.tensor([1, 2, 3])

print(a.shape)
print(b.shape)

#张量a维度拓展
a = a.unsqueeze(0).unsqueeze(0).unsqueeze(-1)
c = c.unsqueeze(0).unsqueeze(0).unsqueeze(-1)
print(a.shape)
print(c.shape)

#张量a维度膨胀
# a = a.expand([2, 2, 3, 2])     #为-1时保持不变
a = a.expand([2, 2, -1, 2])
print(a.shape)
print(a)
#张量c维度膨胀
c = c.repeat([2, 2, 1, 2])   #等同于乘法运算
print(c.shape)
print(c)
