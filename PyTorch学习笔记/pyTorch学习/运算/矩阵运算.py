import torch
#线性层的运算

a = torch.randn(4,564)    # →降低维度为256

#新建矩阵
b = torch.ones(256,564)   #注意：torch写法，(out_channal, in_channal)
c = a@b.t()               #转置操作
print(c.shape)


'''
进行4维运算时，只取最后两维度。
mm不可进行运算，matmul可以进行运算
'''

a = torch.randn(2, 3, 64, 32)
b = torch.randn(2, 3, 32, 16)
d = torch.randn(2, 3, 32, 16)

c = torch.matmul(a,b)
c = a@b                  #两个公式表述相同

print(c.shape)

e = a@d   #自动进行broadcast过程

print(e.shape)

