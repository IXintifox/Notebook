import torch
from torch import Tensor
import math
import matplotlib.pyplot as plt
#函数公式: f(x) = -1.13*x-2.14*x**2+3.15*x**3-0.01*x**4+0.512
#权重输入

t_weight1 = torch.Tensor([13,-5,2,-1]).unsqueeze(1)
t_weight2 = torch.Tensor([16]).unsqueeze(1)



t = torch.linspace(-10,10,1000)
x = 16*torch.sin(t)**3
y = 13*torch.cos(t)-5*torch.cos(2*t)-2*torch.cos(3*t)-torch.cos(4*t)

#函数图像散点图
"""plt.scatter(x,y)
plt.show()"""

#随机数据生成

def get_batch_data(batch_size):
    batch_t = torch.randn(batch_size)
    feature_Max1,feature_Max2 = feature(batch_t)      #X矩阵拼接

    target_Max1,target_Max2 = target(feature_Max1,feature_Max2)    #计算公式
    return feature_Max1,feature_Max2,target_Max1,target_Max2      #返回参数

#处理拼接成[32,4]   w1 w2 w3 w4
def feature(t):
    t = t.unsqueeze(1)
    return torch.cat([torch.cos(t**i) for i in range(1,5)],1),torch.cat([torch.sin(t)**3])

#计算公式
def target(x1,x2):
    return x1.mm(t_weight1),x2.mm(t_weight2)

#多项式模型创建
class PolynomiRegression(torch.nn.Module):
    def __init__(self):
        super(PolynomiRegression, self).__init__()
        self.line1 = torch.nn.Linear(4,1)
        self.line2 = torch.nn.Linear(1,1)
    def forward(self,x1,x2):
        line_1 = self.line1(x1)
        line_2 = self.line2(x2)
        return line_1,line_2



#训练本体
epoch = 50000
batch_size = 32
lr = 0.001

model = PolynomiRegression()
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(),lr)

for i in range(epoch):
    feature_Max1,feature_Max2,target_Max1,target_Max2  = get_batch_data(batch_size)
    out1,out2 = model(feature_Max1,feature_Max2)
    loss1 = criterion(out1,target_Max1)
    loss2 = criterion(out2,target_Max2)
    optimizer.zero_grad()
    loss1.backward()
    loss2.backward()
    optimizer.step()
    if(i%100==0):
        print(r'epoch:{}/{} loss1={},loss2={}'.format(i,epoch,loss1.item(),loss2.item()))
    if(i%1000==0):
        feat1,feat2 = feature(t)
        predict1,predict2 = model(feat1,feat2)
        plt.plot(predict2.squeeze(1).data.numpy(),predict1.squeeze(1).data.numpy(),'r')
        plt.scatter(x,y)
        plt.show()


