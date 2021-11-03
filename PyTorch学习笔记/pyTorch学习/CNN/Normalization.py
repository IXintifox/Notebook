"""
对于图片色块，使用sigmoid函数处理后，可能会有梯度离散的情况出现，使用normalization
处理后，就可以限制色块位于较为集中的范围内。

"""

import torch
from torchvision.transforms import Normalize

x = Normalize(mean=[0.3,0.4,0.5],
              std=[0.2,0.2,0.2])   #运算方式，RGB，R-mean[0]/std[0] G-mean[1]/std[1]

