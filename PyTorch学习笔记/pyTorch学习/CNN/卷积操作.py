import torch
from torch import nn
import torch.nn.functional as F

class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.x = torch.nn.Sequential(
            nn.Conv2d(in_channels=,out_channels=,kernel_size=,stride=),
            nn.AvgPool2d(kernel_size=),
            nn.LeakyReLU(),
            nn.Conv2d(in_channels=,out_channels=,kernel_size=,stride=),
            nn.MaxPool2d(kernel_size=),
            nn.ReLU(),
            F.interpolate(scale_factor=2,mode='nearest')    #放大操作，mode包含多种采样方式。


        )