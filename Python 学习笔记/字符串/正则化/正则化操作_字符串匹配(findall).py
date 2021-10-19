#匹配字符串第一个字符
import re

str1 = 'Ms_Shop ms_shop'
pattern = r'ms\w+'           #匹配ms到后一个字符串
Model = re.match(pattern, str1, re.I)


print (Model)
print (Model.start())     #起始
print (Model.end())      #结束
print (Model.span())    #字符串跨度

print (Model.string)
print (Model.group()) #匹配数据


#匹配搜索到的字符串第一个字符
import re

str2 = 'XXSDSMs_Shop ms_shop'
pattern2 = r'ms_shop'

match = re.search(pattern2, str2)
print(match)   #直接跨越到最后的ms_shop
print(match.span())


#匹配所有的字符串

str3 = 'XXSDS Ms_Shop ms_shop'
pattern2 = 'ms_shop'
match1 = re.findall(pattern2, str3, re.I)    #一次匹配两个，生成列表
print(match1)

for item in match1:    #遍历列表
    print(item)
