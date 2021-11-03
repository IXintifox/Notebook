import torch

class MyLinear(torch.nn.Module):
    def __init__(self,output,input):
        super(MyLinear, self).__init__()

        self.w = torch.nn.Parameter(torch.randn(output,input))   #自动梯度
        self.b = torch.nn.Parameter(torch.randn(output))

    def forward(self,x):
        x = x@self.w + self.b
        return x






