#norm 范数化 不等于 normalize/batch_norm (正则化)      Matrix Norm ≠ Vector Norm
import torch

a = torch.full([2,3],2.)  #torch.ones(3,3)     仅仅可以用浮点计算
b = torch.full([2,3,4],2.)
'''
tensor([[2., 2., 2.],
        [2., 2., 2.]])
'''

print(a.norm(1))     #1的范数，Σ|x|
print(a.norm(2))     #2的范数，各个向量平方和再开根号
print(a.norm(2, dim=1))    #相当于删除该维度的数据

'''
tensor([[[2., 2., 2., 2.],
         [2., 2., 2., 2.],
         [2., 2., 2., 2.]],
        [[2., 2., 2., 2.],
         [2., 2., 2., 2.],
         [2., 2., 2., 2.]]])
         
        [2,3,4]
'''
print(b.norm(2,dim = 0))  #[3,4] 同位置合并运算
print(b.norm(2,dim = 1))  #[2,4] 列同位置运算
print(b.norm(2,dim = 2))  #[2,3] 行同位置运算
#范数化啥，就将其维度抹掉。