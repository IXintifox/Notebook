import torch

# split函数 len分割
x = torch.rand(3,4,5,2)

a,b = x.split(2,dim=1)    #等长分割
print(a.shape,b.shape)

a,b = torch.split(x,[1,2],dim=0)   #固定长度分割,x.split也可
print('a:',a.shape,'b:',b.shape)

#chunk函数
y = torch.rand(3, 4, 5, 2)

c,d,e = torch.chunk(y,3,dim=2)   #y.chunk 也可   3是分割三份，需要三个数据接受，不够的数据减少。
print('c:',c.shape,'d:',d.shape,e.shape)
