import torch

#创建4维度张量
a = torch.rand(1,3,2,4)
print(a)

# transpose操作，调换两个维度
a1 = a.transpose(1,3).contiguous().view(1,3*2*4).view(1,3,2,4)
a2 = a.transpose(1,3).contiguous().view(1,3*2*4).view(1,4,2,3).transpose(1,3)

#判断张量是否相同
print(torch.all(torch.eq(a,a1)))     #all函数，所有内容一致返回true。
print(torch.all(torch.eq(a,a2)))
print(torch.eq(a,a1))  #eq函数比较每一个元素。