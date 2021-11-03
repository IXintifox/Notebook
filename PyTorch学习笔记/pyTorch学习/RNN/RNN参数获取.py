#具有继承作用，考虑到上下语句的继承关系。上一次语境和这一次输入。
'''
ht = tanh(Wi[Whx]Xt+Wr[Whh]ht-1)
yt = Woht

'''

import torch

R1 = torch.nn.RNN(100,10)    #只看最后一层。目标是100dim变为10dim。

x = R1._parameters.keys()
print(x)

#仅看维度
print(R1.weight_ih_l0.shape)      # x → t
print(R1.weight_hh_l0.shape)      # t-1 → t

print(R1.bias_ih_l0.shape)      # 偏置量
print(R1.bias_hh_l0.shape)      # 偏置量



