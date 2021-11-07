import  torch

x = torch.randn(10,3,100)

rnn = torch.nn.RNNCell(input_size=100,hidden_size=20)
h0 = torch.zeros(3,20)

for i in x:
    h0 = rnn(i,h0)

out = rnn(x[9],h0)

print(h0.shape)
print(torch.equal(h0,out))

