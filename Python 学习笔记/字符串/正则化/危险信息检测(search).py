#危险字符串的检测

import re

#c_put = r'(黑客)|(Trojan)|(抓包)|(监听)'

c_put = r'(黑客|Trojan|抓包|监听)'             #两种方法皆可     >>>>>注：当^仅仅匹配字符串开始，$仅仅匹配字符串结尾

put1 = 'XXX是程序员XXXXXXXXXX黑客XXXXXXXXXXTrojanXXXXX'

match = re.search(c_put, put1)


print(match)

if (bool(match)==1):
    print('危险信息')

else :
    print('安全信息')

