import torch

#topk使用方法
a = torch.rand(3,4)

print(a)
print(a.topk(3))    #提供每一行最大的三个数
print(a.topk(3,largest = False))    #提供最小的数


# kthvalue
print(a.kthvalue(2,keepdim = True))  #提供每一行排名第2小的数，只能是小。

# compare  比较符号
x = torch.randn(3,4,5)
y = torch.randn(3,4,5)
print((x>0).int())
print(torch.gt(x,0))    #表示大于该数

print(torch.eq(x,y))
print(torch.equal(x,y))

