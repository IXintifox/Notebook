import torch
from torch import nn
from torch.nn import *


class LeNet(nn.Module):

    def __init__(self):

        super(LeNet, self).__init__()
        self.model = Sequential(
            #
            Conv1d(in_channels=3, out_channels=6, kernel_size=5, stride=4),    #数据长度31
            AvgPool1d(kernel_size=2, stride=1),                                #长度为30
            Conv1d(in_channels=6, out_channels=16, kernel_size=5, stride=4),   #长度为7
            AvgPool1d(kernel_size=2, stride=1),                                #长度为6
            Conv1d(in_channels=16, out_channels=120, kernel_size=2, stride=1), # kernel_size = 2  长度为5
            Flatten(),
            Linear(in_features=600, out_features=84),
            Linear(in_features=84, out_features=2)
        )

    def forward(self, x):
        x = self.model(x)
        return x


lenet = LeNet()
print(lenet)
input = torch.ones(64, 3, 128)
output = lenet(input)
print(output.shape)
