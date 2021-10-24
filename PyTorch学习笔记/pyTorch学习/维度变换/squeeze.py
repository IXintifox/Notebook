# 维度缩减 squeeze
import torch

a = torch.Tensor(1, 1, 3, 1)
print(a.size())
print(a.shape)

print(a.squeeze().shape)   #没有数据时，将可以合并的维度合并
print(a.squeeze(2).shape)  #没有变化
print(a.squeeze(-2).shape)

'''
output:

torch.Size([1, 1, 3, 1])
torch.Size([1, 1, 3, 1])
torch.Size([3])
torch.Size([1, 1, 3, 1])
torch.Size([1, 1, 3, 1])
'''