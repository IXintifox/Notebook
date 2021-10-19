#当sigmoid 函数趋于-∞和∞时，梯度可能会出现消失现象。

import torch

a = torch.linspace(-100,100,10)
print(a)
x = torch.sigmoid(a)
print(x)
'''
tensor([0.0000e+00, 1.6655e-34, 7.4564e-25, 3.3382e-15, 1.4945e-05, 9.9999e-01,
        1.0000e+00, 1.0000e+00, 1.0000e+00, 1.0000e+00])
出现梯度消失现象
'''