#tanh函数，可以通过sigmoid函数变化而来。
#tanh = 2sigmoid(2x)-1    求导后 tanh' = 1-tanh^2(x)
import torch

a = torch.linspace(-2,2,10)
b = torch.tanh(a)
print(b)


#函数图像
import matplotlib.pyplot as plt
import math
import numpy as np
x = torch.arange(-5,5,0.1)
t = []
for i in x:
    y = math.tanh(i)
    t.append(y)

plt.plot(x,t,label='tanh')
plt.xlabel = ('x')
plt.ylabel = ('y')
plt.ylim(-1.5,1.5)
plt.legend()
plt.show()
