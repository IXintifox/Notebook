import torch
from torch import nn

rnn = nn.RNNCell(input_size=100,hidden_size=20)

p = torch.randn(10,3,100)
x = torch.zeros(3,20)      #第一个隐藏层
for i in p:
    x = rnn(i,x)

print(x.shape)