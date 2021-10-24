import torch
a = torch.tensor([0,1,2],requires_grad=True,dtype=torch.float)

y = 3*a
print(y[0].backward(retain_graph=True))
x = torch.autograd.grad(y[1],a)
print(y)
print(x)

