import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)

y1 = x**2
y2 = x*2

plt.figure(num=5,figsize=(10,5))    #图像名字
plt.plot(x,y1,color='green')
plt.plot(x,y2,color='red',linestyle='--',linewidth=2)     #参数设定

plt.figure()     
plt.plot(x,y2)
plt.show()     #输出图像，同时输出，仅使用一个即可。