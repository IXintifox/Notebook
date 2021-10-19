list = "@AAA @BBB @CCC @DDD"

# count方法，查找数量

print(list.count('@'))

# find方法，寻找第一个

print(list.find('@'))
print(list.find('@', 5))   #  从第5个开始寻找,包括第五个，索引带空格
print(list.rfind('@'))    #从右面开始找

# index方法，没有会报异常，相比于find

print(list.index('@'))  #  包括从右寻找，rindex()
print(list.index('@', 5))

# 判断str第一个是否为要求
print(list.startswith('A'))
print(list.startswith('@'))

# 判断最后一个是否为要求
print(list.endswith('D'))
print(list.endswith('@'))
