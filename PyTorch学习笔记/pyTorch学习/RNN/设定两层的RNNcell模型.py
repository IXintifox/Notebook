import torch
from torch import nn

rnn1 = torch.nn.RNNCell(100,30)    #第一个RNN神经元
rnn2 = torch.nn.RNNCell(30,20)     #第二个RNN神经元
hd1 = torch.zeros(3,30)
hd2 = torch.zeros(3,20)

x = torch.randn(10,3,100)
for i in x:
    h1 = rnn1(i,hd1)
    h2 = rnn2(h1)

print(h2.shape)