class Geese:
    '''雁类'''
    __neck = "脖子较长"                       # 类属性（脖子）
    wing = "振翅频率高"                     # 类属性（翅膀）
    leg = "腿位于身份的中心支点，行走自如"  # 类属性（腿）
    number = 0                              # 编号


#①访问限制方法
print(Geese._Geese__neck)

#②访问限制方法
geese = Geese()
print(geese._Geese__neck)


