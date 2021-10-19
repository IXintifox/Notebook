class film:

    lit = ['A', 'B', 'C', 'D']            #定义列表

    def __init__(self, name):
        self.__name = name

    @property                          #第一次赋值走这
    def fil(self):
        return self.__name

    @fil.setter                        #多次赋值走这
    def fil(self, value):
        if value in film.lit:
            self.__name =  ('准备播放：{}   请稍后'.format(value))   #已经返回值

        else:
            print('该元素不在列表中')


flm = film('A')       #第一次赋值
print(flm.fil)

#修改值
flm.fil = 'F'       #不在列表中
flm.fil = 'B'
print(flm.fil)

