import torch

#多层LSTM

x = torch.rand(10,3,100)

rnn = torch.nn.LSTM(input_size=100,hidden_size=30,num_layers=4)

c0 = torch.zeros(4,3,30)                               # (num_layer,batch_size,h)
h0 = torch.zeros(4,3,30)

out,(c0,h0) = rnn(x,[c0,h0])

print(out.shape,c0.shape,h0.shape)


#多层LSTM Cell形式

y = torch.rand(10,3,100)
lstm_cell1 = torch.nn.LSTMCell(input_size=100,hidden_size=30)
lstm_cell2 = torch.nn.LSTMCell(input_size=30,hidden_size=20)

c0 = torch.zeros(3,30)                               # (num_layer,batch_size,h)
h0 = torch.zeros(3,30)
c1 = torch.zeros(3,20)                               # (num_layer,batch_size,h)
h1 = torch.zeros(3,20)

for i in y:

    h0,c0 = lstm_cell1(i,[c0,h0])
    h1,c1 = lstm_cell2(h0,[c1,h1])

print(c1.shape,h1.shape)