import torch
from torch import Tensor
import math
import matplotlib.pyplot as plt
#函数公式: f(x) = -1.13*x-2.14*x**2+3.15*x**3-0.01*x**4+0.512
#权重输入

x_weight = torch.Tensor([-1.13,2.14,3.15,-0.01]).unsqueeze(1)
b = torch.Tensor([0.512])


x = torch.linspace(-2,2,50)
y = -1.13*x-2.14*torch.pow(x,2)+3.15*x**3-0.01*x**4+0.512

#函数图像散点图
"""plt.scatter(x,y)
plt.show()"""

#随机数据生成

def get_batch_data(batch_size):
    batch_x = torch.randn(batch_size)
    feature_Max = feature(batch_x)      #X矩阵拼接
    target_Max = target(feature_Max)    #计算公式
    return feature_Max,target_Max      #返回参数

#处理拼接成[32,4]   w1 w2 w3 w4
def feature(x):
    x = x.unsqueeze(1)
    return torch.cat([x**i for i in range(1,5)],1)

#计算公式
def target(x):
    return x.mm(x_weight)+b.item()

#多项式模型创建
class PolynomiRegression(torch.nn.Module):
    def __init__(self):
        super(PolynomiRegression, self).__init__()
        self.line1 = torch.nn.Linear(4,1)
    def forward(self,x):
        line_d = self.line1(x)
        return line_d



#训练本体
epoch = 10000
batch_size = 32
lr = 0.001

model = PolynomiRegression()
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(),lr)

for i in range(epoch):
    b_x,b_y = get_batch_data(batch_size)
    out = model(b_x)
    loss = criterion(out,b_y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if(i%100==0):
        print(r'epoch:{}/{} loss={}'.format(i,epoch,loss.item()))
    if(i%1000==0):
        predict = model(feature(x))
        plt.plot(x,predict.squeeze(1).data.numpy(),'r')
        plt.scatter(x,y)
        plt.show()


