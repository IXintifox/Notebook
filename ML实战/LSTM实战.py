import pandas as pd
import torch
dataset = pd.read_csv('G:\笔记\ML实战\waimai_10k.csv',engine='python',header=None)

print(dataset.shape)
print(dataset.info)         #数据集信息获取
print(dataset.describe(),'\n')    #数据集描述
print(dataset.columns)
print(dataset.head)

#统计各个类别
print(dataset[0].value_counts())

#测试集保存
dataset.sample(1000).to_csv('test_sample.csv',header=False,index=None)

#标签样本设定
from torchtext import data

