
set1 = {'A', 'B', 'C', 'D', 'E'}
set2 = {'C', 'D', 'E', 'F', 'A'}


set3 = ('交集', set1 & set2)
set4 = ('并集', set1 | set2)
set5 = ('差集', set1 - set2)    # set1有的set2也有的减掉，保留set1
print('交集：{}\n并集：{}\n 差集：{}'.format(set3, set4, set5))
