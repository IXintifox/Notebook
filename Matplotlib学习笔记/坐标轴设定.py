import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)

y1 = x**2
y2 = x*2

plt.figure(num=5,figsize=(10,5))    #图像名字
plt.plot(x,y1,color='green')
plt.plot(x,y2,color='red',linestyle='--',linewidth=2)     #参数设定

#参数设定
plt.xlim(-2,2)
plt.ylim(-2,2)        #轴范围
plt.xlabel('X')
plt.ylabel('Y')       #轴标签

new_ticks = np.linspace(-3,3,10)
plt.xticks(new_ticks)         #坐标轴数据替换
plt.yticks([-1,0,1,3],[r'$bad$',r'$normal$',r'$good$',r'$\beta$'])      #转义输出，可以使用标准α输出，字母替换数字

plt.show()    #图片输出