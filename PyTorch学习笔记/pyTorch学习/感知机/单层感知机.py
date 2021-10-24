import torch
import torch.nn.functional as F

x = torch.randn(1,10)    #节点
w = torch.randn(1,10,requires_grad=True)    #权值

o = torch.sigmoid(x@w.t())

loss = F.mse_loss(torch.ones(1,1),o)     #torch ones是输出目标值，[1]
gra = torch.autograd.grad(loss,w)      #损失求导
print(gra)



