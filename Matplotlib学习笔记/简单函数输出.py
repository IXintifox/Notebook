import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)   #x∈[-1,1] 共50个数据
y = x*2

plt.plot(x,y)
plt.show()

