#双层RNN
import torch

rnn = torch.nn.RNN(input_size=100,hidden_size=20,num_layers=2)
x = rnn._parameters.keys()
print(x)
#参数验证
print(rnn.weight_ih_l0.shape, rnn.weight_ih_l1.shape)     #第一层为100，第二层20 无需转换，因为保留了memory
print(rnn.bias_ih_l0.shape)    #最终变为20

#多层RNN
rnn_m = torch.nn.RNN(input_size=100,hidden_size=30,num_layers=4)
y = rnn_m._parameters.keys()
print(y)
print(rnn_m.weight_ih_l0.shape, rnn_m.weight_ih_l1.shape, rnn_m.weight_ih_l3.shape) #第一层发生转换

i = torch.randn(10,3,100)     #传入张量，X总

out,h = rnn_m(i)
print(out.shape,h.shape)  #out为最终全部输出，h为每一层的输出。

