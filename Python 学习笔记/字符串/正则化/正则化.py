#行定位符
"""

行定位符：
^+字符：以该字符开始
$+字符：以该字符终止
\b 可匹配开始&结束
\w 匹配字母数字下划线汉字
\W 匹配除\w以外全部
\d 匹配数字
+* 例如：\w* 可以不限数量

"""


#限定符


"""

例如：^\d{8}$    >>>>> 开始和结尾 ^/$  \d 表示数字 {8} 限制输入的字符数量为8
？匹配前一字符一次或者零次 Goo?gle 结果为>>>>>  Gogle/Google 
+ 匹配前一字符一次或多次  Goo+gle 结果为>>>>>  Google/Gooo....gle
* 匹配前一字符零次或多次  Goo*gle 结果为>>>>>  Gogle/Gooo....gle
{n,m} 匹配数量可控
特殊字符匹配 使用[.,!]
寻找字母数字 [A-Z0-9a-z]

"""

#排除字符

"""

[^正则化]  排除字符中，使用^表示

"""

#选择匹配数字

"""

#身份证的匹配  包括15位 18位（校验为数字或者字符）
(^\d{15}$)|(^\d{18}$)|(^\d{17})(^\d|X|x)$   #该式子称为模式字符串

#IP地址的匹配
[1-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}

"""

#分组正则化

"""

(four|six)th    >>>>>> fourth & sixth
#分组重复操作 得到IP
[1-9{1,3}](.\[0-9]{1,3}){3}

"""

