from torch import nn
from torch.nn import *

class LeNet(nn.Module):

    def __init__(self,finger):
        super().__init__()
        self.layer1 = Conv1d(in_channels=,out_channels=6,kernel_size=5,stride=4)
        self.layer2 = AvgPool1d(kernel_size=2,stride=1)
        self.layer3 = Conv1d(in_channels=6,out_channels=16,kernel_size=5,stride=4)
        self.layer4 = AvgPool1d(kernel_size=2,stride=1)
        self.layer5 = Conv1d(in_channels=16,out_channels=120)
        self.flatten = Flatten()
        self.layer6 = Linear(out_features=84)
        self.layer7 = Linear(84,2)

    def forward(self,x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        x = self.layer4(x)
        x = self.layer5(x)
        x = self.flatten(x)
        x = self.layer6(x)
        x = self.layer7(x)

