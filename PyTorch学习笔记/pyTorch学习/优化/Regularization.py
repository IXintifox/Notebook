import torch
# L1 regularization cross: Pytorch非内部存在

regularization_loss = 0
for param in model.parameters():
    regularization_loss = torch.sum(torch.abs(param))

loss = classify_loss + 0.01*regularization_loss

optimizer.zero.grad()    #梯度清零
loss.backward()          #损失反向传播
optimizer.step()         #整个模型的更新



#L2 regularization     优化器优化

net.map()   #调用的神经元函数
optimizer = optim.SGD(net.paramaters(),lr=learning_rate,weight_dacay=0.01)   #权重衰减优化

optimizer.zero_grad()
loss.backward()
optimizer.step()

