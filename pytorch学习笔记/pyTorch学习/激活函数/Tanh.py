#tanh函数，可以通过sigmoid函数变化而来。
#tanh = 2sigmoid(2x)-1    求导后 tanh' = 1-tanh^2(x)
import torch

a = torch.linspace(-2,2,10)
b = torch.tanh(a)
print(b)
