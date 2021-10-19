import torch
from torch import nn
from torch.nn import *


class LeNet(nn.Module):

    def __init__(self):
        super(LeNet, self).__init__()
        self.model = Sequential(
            Conv1d(in_channels=3, out_channels=32, kernel_size=5, stride=1 ),
            AvgPool1d(kernel_size=2),
            Conv1d(in_channels=32, out_channels=64, kernel_size=2, stride=1),
            Flatten(),
            #Linear(in_features=256, out_features=28),
            #Linear(in_features=28, out_features=10)
        )

    def forward(self, x):
        x = self.model(x)
        return x


lenet = LeNet()
x = torch.ones(2, 3, 1*10)     #( , in_channal,)
p = lenet(x)
print(p.shape)
print(x)

