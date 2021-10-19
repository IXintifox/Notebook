#值传递，实参不变，引用传递，实参改变。

def function(obj):
    obj += obj


x = 'ABC'
xl = ['A','B','C']

function(x)
print(x)     #>>>>ABC    值传递不变
function(xl)
print(xl)    #>>>>['A','B','C','A','B','C']      引用传递改变

#参数位置需一致，如使用关键字，则无需一致。
#可以于调用括号()中定义参数的值  function(obj = 'XXX'):提前定义好

#可变参数的传递

    #列表
def coffee(*drink):
    print('喜欢的饮品')
    for item in drink:
        print(item)

coffee('A','B','C')
'''
两种传递方式
'''
drk = ['A','B','C']
coffee(*drk)

    #字典

def coffee(**drink):

    for item,t in drink.items():
        print('{}喜欢的饮品是{}'.format(item,t))

coffee (A='1',B='2',C='3')         #前面无需使用引号
'''
两种传递方式
'''
drk = {'A': '1', 'B': '2', 'C': '3'}
coffee(**drk)
