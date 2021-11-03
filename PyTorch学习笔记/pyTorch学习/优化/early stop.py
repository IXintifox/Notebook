"""
当validation 下降时，提前停止。

drop_out 概率断掉几个神经元。


"""

import torch

torch.nn.Linear(784,200)
torch.nn.Dropout(0.5)    #概率断掉一半  ,中间断掉一半
torch.nn.ReLU()
torch.nn.Linear(200,200)

#tf.nn.Dropout (保持不断的概率）
#torch.nn.Dropout(断的概率)

#test时要全部用上，不能断开
net_drop.eval()  #切换模式

"""
stochastic  随机但满足分布N(0,x)
处理大量数据，在所有数据梯度上面的数据集改成在batch上面的梯度。  常用
deterministc 与f(x)一一对应

"""
