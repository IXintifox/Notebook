import torch
import torch.nn.functional as F

x = torch.randn(1,789)
w = torch.randn(10,789)

lofit = x@w.t()

Q = torch.tensor([0.98,0.01,0,0,0.01])     #softmax之后

pred = F.softmax(lofit,dim=1)
pred_log = torch.log(Q)
print(pred_log.shape)


#pre_out = F.cross_entropy(Q.unsqueeze(0),torch.tensor([0]))
#pre_out1 = F.nll_loss(pred_log.unsqueeze(0),torch.tensor([0]))
####当output = torch.tensor为0时，与交叉熵运算结果相同。  取出的0号元素。
#print(pre_out)
#print(pre_out1)

list1 = []
for i in range(5):
    pre_out = F.nll_loss(pred_log.unsqueeze(0),torch.tensor([i]))  #output指取出的值
    list1.append(pre_out)
print(list1)



