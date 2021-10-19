import torch



input = torch.randn(88, 66, 99, 33)

weight = torch.randn(19, 66, 7, 9)
bias = torch.empty(19)   #19个卷积核，生成19个0的函数
print(input, weight)
output = torch.conv2d(input, weight, bias)

print(bias)

print(output.shape)