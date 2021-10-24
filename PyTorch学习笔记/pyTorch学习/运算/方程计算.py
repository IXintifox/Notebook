import torch
import math
import matplotlib.pyplot as plt
x = torch.arange(-10, 10, 0.1)

y = []
for t in x:
    y_1 = 1 / (1 + math.exp(-t))
    y.append(y_1)
plt.plot(x, y, label="sigmoid")

plt.xlabel("x")
plt.ylabel("y")
plt.ylim(0, 1)   #坐标轴y轴的范围
plt.legend()     #调用文字
plt.show()
