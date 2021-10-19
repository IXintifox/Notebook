#where函数   where(condition ,x,y) 用于大量参数来自不同来源
import torch

a = torch.rand(2, 3)
x = torch.zeros(2, 3)
y = torch.ones(2, 3)

z = torch.where(a > 0.5, x, y)  #大于0.5为0
print(a)
print(z)

#gather 函数 gather(input,dim,index)     查表，找到一个匹配的label。
#随机定义一个张量，取出其最大的四个数，并使用相应的label对数进行替换，输出该矩阵。

b = torch.randn(6, 20)
b_max4 = b.topk(4, dim=1)
print(b_max4)
p = torch.arange(20) + 100
p = p.expand(6, 20)
print(p)
out = torch.gather(input = p,dim=1,index=b_max4[1])  #index需为整数
print(out)






