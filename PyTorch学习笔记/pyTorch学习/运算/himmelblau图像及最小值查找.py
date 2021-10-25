import numpy as np
import matplotlib.pyplot as plt
import torch

#代码格式化
def himmelblau(x):
    return (x[0]**2+x[1]-11)**2+(x[0]+x[1]**2-7)**2

<<<<<<< HEAD
x = np.arange(-6, 6, 0.1)    #间隔0.1，范围为-6-6
y = np.arange(-6, 6, 0.1)    #y轴
=======
x = np.arange(-6, 6, 0.1)
y = np.arange(-6, 6, 0.1)
>>>>>>> Notebook/master
X, Y = np.meshgrid(x, y)     #相当于生成两个图片,匹配XY轴

print(X.shape, Y.shape)
Z = himmelblau([X,Y])

fig = plt.figure('HIM')
ax = fig.gca(projection ='3d')    #不再使用
ax.plot_surface(X, Y, Z)
ax.view_init(60, -30)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

#寻找全局最小值
x = torch.tensor([6., 0.],requires_grad=True)     # 初始位置
optimizer = torch.optim.Adam([x],lr=1e-3)

for i in range(20000):
    pred = himmelblau(x)
    optimizer.zero_grad()     #每一次将loss中的weight清零，因为此不是求损失。梯度清零
    pred.backward()    #获得一个梯度信息
    optimizer.step()   #梯度信息优化更新。

    '''
     if i % 200 == 0:
        print(i, x.tolist(), pred.item())     # tolist将数组和矩阵转换成列表

    '''


