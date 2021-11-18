import  random
from random import randint

random.seed(332)    #固定生成随机数的数量，神经元数量固定。
signals = {'嗅觉信号':'闻','听觉信号':'听'}
#定义神经网络

#突触携带数据
class Neuron:
    def __init__(self,signal_type):
        self.signal_type = signal_type   #>> self.signal_type = ‘嗅觉信号’

#判断是否激活神经网络
    def active(self,x):

        if self.signal_type == x.signal_type:
            return signals[self.signal_type]+':'+x.data
        else :
            return signals[self.signal_type]+':'+'没有信号'

#神经网络信号输入
class Signal_input:
    def __init__(self,signal_type,data):
        self.signal_type = signal_type
        self.data = data



"""#数据传入
test = Signal_input('听觉信号','奇特的味道')       #将Signal_input当作x输入到active里面
print(Neuron('嗅觉信号').active(test))        #>>Neuron文本输入6,7,8     active文本输入test"""

#脑皮层的构建
#相关函数的调用


class HearbrainArea:
    def __init__(self,num):
        self.neurons = [Neuron('听觉信号') for i in range(num)]

    def process(self,x):
        print('听觉皮层正在处理'+':'+ x.data)


class SmellbrainArea:
    def __init__(self, num):        #7000
        self.neurons = [Neuron('嗅觉信号') for i in range(num)]

    def process(self, x):
        print('嗅觉皮层正在处理' +':'+ x.data)

class Brain:
    def __init__(self):
        self.hear_area = HearbrainArea(randint(2000,10000))
        self.smell_area = SmellbrainArea(randint(2000,10000))   #7000

    def process(self,x):
        return {'嗅觉信号':lambda p:self.smell_area.process(x),'听觉信号':lambda p:self.hear_area.process(x)}[x.signal_type](x)


#调用
brain = Brain()
hear = Signal_input('听觉信号','好美的歌！')
brain.process(hear)