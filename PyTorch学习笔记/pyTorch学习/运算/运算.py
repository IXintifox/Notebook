'''
加减乘除的使用
add +
div /
mul *
sub -
效果相同
'''
#矩阵的运算  *element-wise    矩阵乘法： matrix matmul
import torch
a = torch.tensor([[3.,3.],[3.,3.]])
b = torch.ones(2,2)

c = a*b     #一般乘法 各个元素相乘
print(c)

#d,e,f具有相同的矩阵乘法效果。
d = a@b
print(d)

e = torch.mm(a,b)
f = torch.matmul(a,b)
print(e,'\n',f)

#其他运算
x = torch.full([3, 3], 4)
print(x**2)
print(x.pow(2).sqrt().rsqrt())  #平方开平方，开平方的导数
print(torch.exp(x))       #e的次方
print(torch.log(torch.exp(x)))     #log默认以e为底


#近似值函数
y = torch.tensor(3.14)
print(y.floor(), y.ceil(), y.round(), y.trunc(), y.frac())
#向下取整，向上取整， 四舍五入   trunc 裁剪，整数与小数 frac为小数

#clamp函数
z = torch.rand(3,3)*20

print(z)
print(z.max(),z.median())

z = z.clamp(0,4)     #大于范围的变成4  clamp(min,max)
#clamp(4) 小于4的都变成4   clamp(min)
print(z)


