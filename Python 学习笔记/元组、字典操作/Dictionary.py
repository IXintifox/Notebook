#字典的创建
    #空列表创建方法
dic1 = {}
dic2 = dict()

print('dic1 = {} dic2 = {}'.format(dic1, dic2))

    #元组的字典对映
tuple1 = ('1', '2', '3', '4')
tuple2 = ('A', 'C', 'E', 'G')

dic3 = dict(zip(tuple1, tuple2))   # 分别匹配 ( key : value )
print(dic3)

    #创建值为空的列表
tuple3 = ('A', 'C', 'E', 'G')
dic4 = dict.fromkeys(tuple3,'1')  #后面赋值
print(dic4)
# >>>> {'C': None, 'E': None, 'G': None, 'A': None}

    #字典生成式
        #遍历字典
dic5 = {h: g+' number' for h, g in dic3.items() }    #zip(A,B)生成的是元组式，如遍历字典中既要键又要值，需要使用itmes()函数。
print(dic5)

        #随机数生成字典
import random

dic = {x: random.randint(1,100) for x in range(5)}
print(dic)

    #字典生成补充



#字典的输出

    #判断是否存在
dic5 = {'A': '1'}
print('X的值是：', dic5['X'] if 'X' in dic5 else '没有此参数')    #判断 dict['Key'] 是否存在。

    #遍历字典
for key, value in dic3.items():      #itmes列出的对应元组。（'key','item '）
    print('{}的值为{}'.format(key, value))

#字典的修改

    #添加键直接 dict['key'] = value

    #元素删除 del dict['key'] 删除对应键值，加一个if，防止错误。

