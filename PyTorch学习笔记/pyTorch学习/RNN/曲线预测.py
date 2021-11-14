import torch
import numpy as np
import matplotlib.pyplot as plt

num_time_steps = 50
hidden_size = 16
input_size = 1
output_size = 1
lr = 0.0001
snum = 3

# 神经网络层的构建
class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.rnn = torch.nn.RNN(input_size=input_size, hidden_size=hidden_size,  num_layers=1,  batch_first=True)     # RNN神经网络的构建，数量为1层，并且输入数据batch_size为第一个值
        for p in self.rnn.parameters():
            torch.nn.init.normal_(p,mean=0.0,std=0.001)                                                               # 对RNN中的每个参数使用normal标准化
        self.linear = torch.nn.Linear(hidden_size, output_size)                                                       # 线性化，最终输出线性层

    def forward(self, x, hidden_prev):                                                                                # 参数传入 x, hid_pre         x = [1,49,1]    hid_pre = [1,1,20]   x = [batch,sque,char]   hid_pre = [batch,sque,hidden_size]
        out, hidden_prev = self.rnn(x, hidden_prev)                                                                   # 获得rnn的返回值    返回的 out=  *[1,49,20](batch,sque,hidden_size)  hidden_prev=  *[1,1,20]
        out = out.view(-1,hidden_size)                                                                                # 合并除了隐藏层其他层            out合并为 [49,20]    参入线性化转化 *[49,1]
        out = self.linear(out)                                                                                        # hidden对接hidden             out还原[1,49,20]
        out = out.unsqueeze(dim=0)                                                                                    #第一位展开 1   （1，other,output_size）   返回out与hidden_prev
        return out, hidden_prev

#操作
model = Net()                                                                                        #调用神经网络模组
criterion = torch.nn.MSELoss()                                                                       #使用MSEloss参数进行损失计算
optimizer = torch.optim.Adam(model.parameters(), lr)                                                 #使用Adam进行参数优化(梯度下降) 每一个参数都参与，优化率为lr

hidden_prev = torch.zeros(1, 1, hidden_size)                                       #h0 = [1,1,h_s]     常见文字输入[10,3,100]  [1,3,20]    batch = 3  换位[3,1,20]   此处数据为[1,1,h_s]         *假设输入数据为[1,1,20]
#训练次数
for iter in range(6000):                                                  # 训练6000次
    start = np.random.randint(snum, size=1)[0]                                     # 什么都不输入，默认数值按照最大值处理  后面的[]是为了获得数组中的数字，随机得到一个数字。
    time_step = np.linspace(start, start + 10, num_time_steps)                     # 时间步长，在取值范围内均匀切割值，此时数据shape为[num_time_steps]。
    # 学习数据

    data = np.sin(time_step)                                                       # 获得sin曲线的y值 此时输入数据shape为[num_time_steps]       最终需要规范数据为[1,nts,1]

    data = data.reshape(num_time_steps, 1)                                         # 修改数据类型为[nts,1]
    # 数据集覆盖，
    x = torch.tensor(data[:-1]).float().view(1, num_time_steps - 1, 1)             # np转tensor类型，获得数据集x，数据集包含类型为[1,nts-1,1],范围为[0,nts-1]
    y = torch.tensor(data[1:]).float().view(1, num_time_steps - 1, 1)              # np转tensor类型，获得数据集y，数据集包含类型为[1,nts-1,1],范围为[1,nts]     验证作用

    output, hidden_prev = model(x , hidden_prev)                                   # 数据传入，x训练集，h_p为h0    => 跳转到第13行                                                                 *假设输入数据为[1,49,1]
    hidden_prev = hidden_prev.detach()                                             # hidden_prev获得，网络参数不变

    loss = criterion(output,y)                                                     # 计算loss，           %%%%%%暂时未知， 预测值 真实值   x预测的是下一个点，所以与下一个点作差值
    model.zero_grad()                                                              # 梯度清零
    loss.backward()  # 损失反向传播

    #解决梯度爆炸
    """   
    for p in model.parameters():
           if p.grad.norm() > 0.01:
               torch.nn.utils.clip_grad_norm_(p,0.01)
    """

    optimizer.step()                                                               # 优化每一步函数

    if iter % 300 == 0:                                                            # 输出步骤优化
        print(iter, loss.item())

#测试数据

start = np.random.randint(snum, size=1)[0]                                                          # 测试数据集生成
time_step = np.linspace(start, start + 10, num_time_steps)  # 时间步长，在定义范围内均匀切割值。           # 同上
# 学习数据

data = np.sin(time_step)                                                                            # 同上

data = data.reshape(num_time_steps, 1)                                                              # 同上
# 数据集覆盖，
x = torch.tensor(data[:-1]).float().view(1, num_time_steps - 1, 1)                                  # 同上
y = torch.tensor(data[1:]).float().view(1, num_time_steps - 1, 1)                                   # 同上


#测试环节
predictions = []                                                                         # 设定空列表
input = x[:,0,:]                                                                         # 保留 x = [1,49,1] 变为 [b,1] 此时使用的为测试集  [1,1]  ???
print(hidden_prev)
for i in range(x.shape[1]):                                                              # 包含最后每一个元素的第一个信息
    input = input.view(1, 1, 1)                                                          # 规范化大小
    pred,hidden_prev = model(input,hidden_prev)                                          #每次更新一个点，将输入每一个点结果返回。
    input = pred                                                                         #此次预测值是下一次的输入。
    predictions.append(pred.detach().numpy().ravel()[0])                                 #将输出的结果每不更新处理，然后转化为numpy，扁平化处理

x = x.data.numpy().ravel()
y = y.data.numpy()
plt.scatter(time_step[:-1], x.ravel(), s=90)
plt.plot(time_step[:-1],x.ravel())

plt.scatter(time_step[1:],predictions)
plt.show()