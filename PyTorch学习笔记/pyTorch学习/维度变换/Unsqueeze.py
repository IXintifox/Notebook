import torch

x = torch.rand(4, 3, 10, 10)
print(x.unsqueeze(0).shape)   #在0前面插入数值
print(x.unsqueeze(4).shape)   #在3位后面插入

y = torch.Tensor(4, 5)              #创建了4*5随机数的张量
z = torch.Tensor([4.2, 3.4])        #创建了一个一位张量，该张量为[2]
print(y.unsqueeze(-1))              #[4,5,1]   变成4组数据，5行1列
print(y.unsqueeze(0).shape)         #[1,4,5]
print(z.unsqueeze(0))               #tensor([[4.2000, 3.4000]])
print(z.unsqueeze(0).shape)         #torch.Size([1, 2])
print(z.unsqueeze(-1))              #数据包为tensor([[4.2000],[3.4000]])
print(z.unsqueeze(-1).shape)        #torch.Size([2, 1])

print('\n\n\n', '=_=_'*20)

#实例分析，张量计算
a = torch.Tensor(1,1,3,1)
b = torch.Tensor(3)
print(a.shape,b.shape)
b = b.unsqueeze(0).unsqueeze(-1).unsqueeze(0)
print(a.shape,b.shape)
c = a+b
print(c.shape)