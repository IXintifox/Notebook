"""
Broadcasting 自动扩张函数
    扩张步骤：1.unsqueeze
            2.expand(节省内存)

具体案例：
Ⅰ.分数增加
1.设定数据集[3,32,7]    class:2    student:32     scores:7
2.给每个student scores增加3
3.分析：
    分数为标量,tensor.shape = [1]
    broadcasting函数为从低维开始匹配。
4.常规步骤：
    infor = torch.Tensor(3,32,7)
    add = torch.Tensor([3])

    add = add.unsqueeze(0).unsqueeze(0).expand([3,32,7])
    infor + add 运算

5.boardcasting步骤：
    自动执行unsqueeze与expand,自动匹配。

Ⅱ.其他案例
[4,3,32,32]
+[32,32]      #图片大小确定
+[3,1,1]      #图片为RGB图片，但是大小为1*1
+[1,1,1,1]    #等同于[1],像素抬高




"""