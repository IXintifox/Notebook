import re

info = '中奖号码为：28749873   手机：1394857362'

pattern = r'1[35678]\d{8}'
rep = re.sub(pattern,'1XXXXXXXXXX',info)   #还可加上（替换次数，替换标志位）

print(rep)