#大小写转换
list = 'AbCefG'

    #全部大写
print(list.upper())
print(list.lower())

#去除字符串的空格和特殊字符
list2 = '   @$ssadsds  &@  '
lis = list2.strip(' @$')  #扫到不符合的就停止
lis1 = list2.lstrip(' @')  #rstrip同理
print(lis)
print(lis1)