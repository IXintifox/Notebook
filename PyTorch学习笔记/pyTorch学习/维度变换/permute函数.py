import torch

#创建一个张量

a = torch.rand(2,3,4,5)

#维度调换
a1 = a.transpose(1,3)
print(a1.shape)

#维度恢复
a1 = a1.permute(0,3,2,1)
print(torch.all(torch.eq(a,a1)))