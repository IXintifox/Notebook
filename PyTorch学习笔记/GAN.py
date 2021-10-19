import torch
from torch import nn

import numpy as np
import visdom
import random

p = 400
batch_size = 512
viz = visdom.Visdom()
class Generator(nn.Module):

    def __init__(self):
        super(Generator, self).__init__()

        self.net = nn.Sequential(
            nn.Linear(2, p),
            nn.ReLU(True),
            nn.Linear(p, p),
            nn.ReLU(True),
            nn.Linear(p, p),
            nn.ReLU(True),
            nn.Linear(p, 2),


        )

    def forward(self, z):
        output = self.net(z)
        return output


class Discriminator(nn.Module):

    def __init__(self):
        super(Discriminator, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(2, p),
            nn.ReLU(True),
            nn.Linear(p, p),
            nn.ReLU(True),
            nn.Linear(p, p),
            nn.ReLU(True),
            nn.Linear(p, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        output = self.net(x)
        return output.view(-1)


def data_generator():
