import torch

"""
原理相同，但是由于权重比例不同，最终测试结果不相同。

"""

#数据输入
x = torch.randn(10,3,100)
h0 = torch.zeros(1,3,20)    #RNN输入需要定义第一次输入的张量大小。
h1 = torch.zeros(3,20)


#RNN函数的定义

rnn1 = torch.nn.RNN(input_size=100, hidden_size=20, num_layers=1)


#RNNcell的定义


rnn2 = torch.nn.RNNCell(input_size=100,hidden_size=20)


#数据测试

out1,h = rnn1(x,h0)

for i in x:
    h1 = rnn2(i,h1)

print(torch.equal(out1,h1))

