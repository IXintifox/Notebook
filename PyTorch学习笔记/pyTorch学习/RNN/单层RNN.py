from torch import nn
import torch

rnn = nn.RNN(input_size=100, hidden_size=20, num_layers=1)  # 单层RNN网络定义。；

#传入参数(x,h)  x表示所有内容
x = torch.randn(10, 5, 100)
h0 = torch.zeros(1, 5, 20)

out, h = rnn(x, h0)
print(out.shape, h.shape)      # out 为最后时刻最终memo输出值(10,5,20) h为所有层最后memo状态(1,5,20)


