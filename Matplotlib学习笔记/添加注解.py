import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-10,10,100)
y1 = 1/(1+np.exp(-x))
y2 = np.tanh(x)



plt.figure('sigmoid')

l1 = plt.plot(x,y1,color='orange')
l2 = plt.plot(x,y2,color='blue')

plt.xlabel('x')
plt.ylabel('y')

plt.xlim(-10,10)
plt.ylim(-2,2)

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))   
ax.spines['bottom'].set_position(('data',0))

plt.legend(handles = [l1[0],l2[0]],labels=['Sigmoid','Tanh'],loc='best')

'''
Set a point
'''
x0 = 1
y0 = 1/(1+np.exp(-x0))

xx0 = 1.5
yy0 = np.tanh(xx0)



plt.scatter(x0,y0,color='red',s=30)
plt.plot([x0,x0],[0,y0],color = 'red',linestyle = '--',linewidth = 3)

plt.scatter(xx0,yy0,color='red',s=30)
plt.plot([xx0,xx0],[yy0,0],color='red',linestyle = '--',linewidth = 3)

plt.annotate(r'$1/(1+exp)$',xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='offset points',fontsize=15,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0.2'))

plt.text(-1,1,r'$sigmoid$',fontsize = 17,color = 'red')

plt.show()
