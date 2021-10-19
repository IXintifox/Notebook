#集合的创建

set1 = {'A', 'B', 'C', 'D'}
set2 = set('ABCD')
set3 = set(('ABCD','EFGH'))      #元组转换为集合

print(('创建集合Ⅰ：{} Ⅱ：{} Ⅲ：{}').format(set1, set2, set3))

#元素的删除

set1.remove('B')  #指定删除
set2.pop()
set3.clear()      #使用del set3后集合会变为未定义

print(('集合修改Ⅰ：{} Ⅱ：{} Ⅲ：{}').format(set1, set2, set3))

