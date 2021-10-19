import torch


#2组数据，每组数据包含两行三列。
a = torch.randn(2, 2, 3)    #均值为0，方差为1。
#tensor 张量本身含有的元素
print(a, '\n')
print(a.shape)
'''
tensor([[[ 0.2679,  0.4191, -1.0792],
         [-0.1956,  2.0223,  0.2227]],

        [[ 0.3769,  1.2775,  1.3293],
         [ 1.3216,  1.0440, -1.4764]]]) 
         
a转化为列表为[[[0],[1]],[[0],[1]]]   其中0，1中各包含三个元素。
'''
#获得第一部分的第二个元素
print(a[0][0][1])
#列举元素
print(list(a.shape))

#3-D数据类型[x,y,z]  x相当于单词数，y相当于句子（in_channal）,z相当于编码属
#4-D数据类型[a,b,c,d] batch,in_channal,h.w

#tensor的大小(实际大小)
print(a.numel())
#tensor的维度
print(a.dim())

b = torch.rand(2, 3, 3, 2)
print(b, '\n')
print(b.shape)





