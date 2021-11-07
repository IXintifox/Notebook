import torch
from torch import nn

rnn1 = torch.nn.RNNCell(100,30)    #第一个RNN神经元
rnn2 = torch.nn.RNNCell(30,20)     #第二个RNN神经元
b1 = torch.zeros(3,30)
b2 = torch.zeros(3,20)

x = torch.randn(10,3,100)
for i in x:
    h1 = rnn1(i,b1)
    h2 = rnn2(h1,b2)      #相当于两个RNN连在了一起，因此也要定义一个符合大小的输入量h0
    print(i.shape)

print(h2.shape)