import re

c_put = r'(黑客|Trojan|抓包|监听)'
put1 = 'XXX是程序员XXXXXXXXXX黑客XXXXXXXXXXTrojanXXXXX'

repl = re.sub(c_put, '@_@', put1)
print(repl)