# cat拼接：拼接的维度可以不同
import torch

a = torch.rand(3,5,5)
b = torch.rand(4,5,5)

c = torch.cat([a,b],dim=0)    #合并a,b 合并维度dim = 0

print(c.shape)     #cat时，只能在维度不同的地方加，其他参数必须相同


# stack拼接必须是相同维度
x = torch.rand(4,4)
z = torch.rand(4,4)

y = torch.stack([x,z],dim = 0)
print(y.shape)     #torch.Size([2, 4, 4]) 不合并

m = torch.rand(3,4,5)
n = torch.rand(3,4,5)
k = torch.stack([m,n],dim=2)   #[3,4,2,5]
print(k.shape)
