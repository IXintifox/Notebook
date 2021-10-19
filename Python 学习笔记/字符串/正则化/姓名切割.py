import re
list1 = "@AAA @BBB @CCC @DDD"

model = r'\s*@'    #使用零次或多次空格+@分割
x = re.split(model,list1)
for i in x:
    if i != '':
        print(i)
