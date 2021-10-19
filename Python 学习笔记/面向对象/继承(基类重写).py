class Fruit:                     #定义基类class

    def __init__(self, color='Green'):           #定义一个基类默认参数
        Fruit.color = color                      #赋值

    def harvest(self, color):
        print('The fruit is {}'.format(color))      #使用self.color 也可?
        print('The fruit has been harveste')
        print('ohh,The fruit is {}'.format(Fruit.color))     #使用基类class中的color

class Apple(Fruit):

    color = 'red'       #子类class 中的默认参数

    def __init__(self):
        print('I am apple')
        super().__init__()      #调用父类中的__Init__


class Pear(Fruit):

    def __init__(self, color):
        print('I am pear')
        super().__init__(color)

    def harvest(self, color):
        print('The pear is {}'.format(color))
        print('The pear has been harvested')
        print('ohh,The pear is {}'.format(Fruit.color))



apple = Apple()
apple.harvest(apple.color)

pear = Pear('golden')
pear.harvest('yellow')
