import torch
import torch.nn.functional as F
x1 = torch.randn(1)
w1 = torch.randn(1, requires_grad=True)
b1 = torch.randn(1)

w2 = torch.randn(1, requires_grad=True)
b2 = torch.randn(1)


o1= torch.sigmoid(x1@w1+b1)
o2 = torch.sigmoid(o1@w2+b2)


loss2 = F.mse_loss(o2,torch.ones(1)) #直接求导


gra1 = torch.autograd.grad(loss2, w1, retain_graph=True)
print(gra1)
'''
全连接层求导的验证,此时的函数为sigmoid函数
'''
grat1 = torch.autograd.grad(o2, w1, retain_graph=True)
grat2 = torch.autograd.grad(o2, o1, retain_graph=True)
grat3 = torch.autograd.grad(o1, w1, retain_graph=True)

print(grat1, grat2[0]*grat3[0])










