class Geese:
    '''雁类'''
    neck = "脖子较长"                       # 类属性（脖子）
    wing = "振翅频率高"                     # 类属性（翅膀）
    leg = "腿位于身份的中心支点，行走自如"  # 类属性（腿）
    number = 0                              # 编号

    def __init__(self):
        Geese.number +=1
        print(Geese.neck)
        print(Geese.wing)
        print(Geese.leg)
        print('我是第{}只大雁'.format(Geese.number))

list = []
for i in range(4):
    list.append(Geese())      #将每一次调用的数据储存进列表

print(list)
print('一共{}只大雁'.format(Geese.number))     #可以直接调用类属性，注:运算会发生改变
print(Geese.neck)        #可以直接调用类属性
print(list[2])                  #调用列表中的数据
Geese.beak = '测试项目数据'       #加入新属性
print(Geese.beak)        #可以直接调用加入的属性
print(list[1].beak)         #可以单独调用某一个的属性


