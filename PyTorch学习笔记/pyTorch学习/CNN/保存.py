#保存调用
net = Net()
net.load_state_dict(torch.load('ckpt.mdl'))  #加载
torch.save(net.state_dict(),'ckpt.mdl')   #保存

#train/test 切换

net.train()
net.eval()


#维度打平：全连接层
class Flatten(nn.Module):
    def __init__(self):
        super(Flatten, self).__init__()

    def forward(self,input):
        return input.view(input.size(0),-1)    #保留0项，合并后面所有项目。

    