#@的删除
list1 = "@AAA @BBB @CCC @DDD"
list_s = list1.split(' ')
print('你所@的好友有', end=' ')
for item in list_s:
    print(item[1:], end=' ')


#@的添加
list2 = ["AAA", "BBB", "CCC", "DDD"]
list_n = '@' + ' @'.join(list2)
print(list_n)
