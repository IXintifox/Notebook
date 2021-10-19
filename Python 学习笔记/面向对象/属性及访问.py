class fname:

    def __init__(self,name):
        self.__name = name       #__name中下划线仅作标志作用

    @property                         #转化为属性
    def mation(self):
        return self.__name       #将不可变值返回



film = fname('MEDSR')          #仅可赋值一次
print(film.mation)             #转化为property可以不使用括号