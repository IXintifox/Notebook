import torch
import torch.nn.functional as F

a = torch.tensor([0,1,2],requires_grad=True,dtype=torch.float64)
p = F.softmax(a,dim=0)


x = torch.autograd.grad(p[0],a,retain_graph=True)
print(a)
print(p)

print(x)