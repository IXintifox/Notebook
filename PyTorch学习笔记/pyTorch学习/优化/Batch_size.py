import torch

x1 = torch.rand(6,3,728)
x2 = torch.rand(6,3,28,28)

y = torch.nn.BatchNorm1d(3)
z = y(x1)

print(y.running_mean)    #μ
print(y.running_var)     #σ^2

p = torch.nn.BatchNorm2d(3)
d = p(x2)

#二维张量可以看到的权重
print(p.weight)     #w    (γ)
print(p.bias,'\n')       #β
print(vars(p))      #看到全局的μ和σ^2



