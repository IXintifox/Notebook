
'''
MSE均方差
一般表述形式：Σ(y-y^)^2

loss = Σ[y-(xw+b)]^2  y原-y预测   f(x;w,b)
L2-norm = ||y-(xw+b)||2(下标)   实际计算：  √Σ(y1ij-y2ij)^2   ——————————tensor计算
loss = norm(y-(xw+b))^2   ————————————均值  实现形式 torch.norm(y-prediction,2).pow(2) 抵消norm根号

loss函数求导：
2Σ[y-(xw+b)]*(-x-1)

'''

#auto_grad
import torch
import torch.nn.functional as F
x = torch.ones(1,requires_grad=True)
w = torch.full([1],2., requires_grad=True)
#print(w.type())
mes = F.mse_loss(torch.ones(1),x*w)    #参数(预测值 实际值,)  (1,2)
print('mes',mes)
print(w)

#自动求导

p = torch.autograd.grad(mes, [x])     # 前面的对后面的求导。autograd(预测值，实际参数w1,w2……)
print(p)  #对w输出为2. 对x输出为4.


#backward
mes_1 = F.mse_loss(torch.ones(1),x*w)
q = mes_1.backward()     #自动对梯度求导，并将结果附加在每一个grad中。
e = w.grad   #(x.grad) 对x求导，(w.grad) 对w求导
print(e)




