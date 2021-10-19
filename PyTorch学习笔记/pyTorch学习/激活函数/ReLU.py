#当z<0不响应，当z>0线性相应（x） y = x
import torch

a = torch.linspace(-10,10,20)
b = torch.relu(a)
print(b)  #梯度非常稳定。
