import Calculate     # 调用同文件夹中模块
from add_c import *

print(Calculate.cal(32))

print(plus(3, 4),reduce(5, 3))   # 使用*调用了全部内部函数