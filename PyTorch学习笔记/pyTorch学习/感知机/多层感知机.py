import torch
import torch.nn.functional as F

x = torch.randn(1,4)
w = torch.randn(2,4,requires_grad=True)    #输出对象为两个节点

o = torch.sigmoid(x@w.t())

loss = F.mse_loss(torch.ones(1,2),o)   #对一行两列求导。
gra = torch.autograd.grad(loss,w)     #更符合的权值权值
print(gra)

