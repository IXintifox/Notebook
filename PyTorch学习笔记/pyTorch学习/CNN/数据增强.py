"""
旋转，噪声。

Data argumentation

Flip
rotate
random move crop
GAN
"""
from torchvision import transforms
#实现方法,Flip
dataset(transform = transforms.Compose(
    [transforms.RandomHorizontalFlip(),
     transforms.RandomVerticalFlip(),
     transforms.ToTensor(),
     ]    #ToTensor 张量转换
),shuffle=True)


#rotate
transforms.RandomRotation(15)  # -15 - 0 - 15
transforms.RandomRotation([90,180,270])  # 随机选择

#scale
transforms.Resize([32,32])     #改变成此大小

#Crop Part
transforms.RandomCrop([28,28])   #随机裁剪

#noise  N(0，0.001)
# numpy处理


