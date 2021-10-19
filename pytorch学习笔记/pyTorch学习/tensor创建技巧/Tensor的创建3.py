import torch

#生成不被初始化的数据。
a = torch.empty(2, 3)
print('未初始化数据', a)
T1 = torch.FloatTensor(1, 2, 3, 4)
T2 = torch.IntTensor(1, 2, 3, 4)
print('浮点类型', T1, "\n整型", T2)
#类型查看,设置
print(T1.type(), T2.type())
torch.set_default_tensor_type(torch.DoubleTensor)
b = torch.Tensor([1, 3])
print(b, b.type())

#随机初始化
c = torch.rand(3,3)   # 0，1之间
print(c)
d = torch.rand_like(c) # 0，1再赋值一次
e = torch.randint(1,10,[4,3])    # 从1-9的随机数，后部分使用[]设定tensor的大小(shape)。
print(e)

#torch.normal的用法
f = torch.normal(mean=torch.full([10], 0.), std=torch.arange(1, 0, -0.1))
"""
full 函数中[10]为3*3的数据压缩为一条直线，0.是覆盖[0,0,0,0,0.....],在std中，从1到0，每次减少1
"""
print(f)

# full函数的使用
f1 = torch.full([2,2],7)
print(f1)     # 生成2维张量
f2 = torch.full([],7)
print(f2)     # 生成标量
f3 = torch.full([1],7)
print(f3)     # 生成1维张量

#arange使用
a1 = torch.arange(0,10)   # tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])   不包含最后的数
print(a1)
a2 = torch.arange(0,10,2)   # tensor([0, 2, 4, 6, 8])  第三个数是阶梯
print(a2)

#linspace/logspace的使用
l1 = torch.linspace(0,10,5)   # tensor([ 0.0000,  2.5000,  5.0000,  7.5000, 10.0000]) 第三个数代表数量，包含最后一个数
print(l1)
lo1 = torch.logspace(0,-1,10)   # 两端代表10 0次方及10 的-1次方 分割中间填补函数曲线上的数
print(lo1)

# 生成矩阵的简易方式
t1 = torch.ones(3,3)
t2 = torch.zeros(3,3)
t3 = torch.eye(3,3)  #生成对角矩阵，最多接受两个参数
print(t1,'\n',t2,'\n',t3)
#0转1方法
t4 = torch.ones_like(t2)
print(t4)

#随机打散函数 等同于numpy 的shuffle
r1 = torch.randperm(10)    # 输出0-9，顺序打散。
print(r1)
#####例子
s1 = torch.rand(2,3)
s2 = torch.rand(2,4)
ss = torch.randperm(2)

print(s1,'\n',ss,'\n',s1[ss])  #生成的randperm为[1,0],就按照s1中第一行，第零行的数据排列。


#创建固定值的tensor
x1 = torch.full([3,3],2)
print(x1)