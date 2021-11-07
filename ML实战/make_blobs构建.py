from sklearn.datasets import make_blobs
from matplotlib import pyplot

#使用make_blobs收集散点
data, target = make_blobs(n_samples=100,n_features=2,centers=2,cluster_std=[1.0,4.0])    #target是数据类别的的标签 data是数据的坐标
print(target)
print(data)

pyplot.scatter(data[:,1],data[:,0],c =target)    #data[:,]前面为数据的范围，后面为数据的坐标，0为x 1为y
pyplot.show()