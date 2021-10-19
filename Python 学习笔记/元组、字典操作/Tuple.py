#元组的创建

    #一个元素

str1 = 'intifox',
str2 = 'intifox,'
print ('str1 = {} str2 = {}'.format(str1, str2))

# >>>>tp = ('intifox',)  str = intifox,

    #多个元素（元组生成式）
import random
tuple_A = (random.randint(0,100) for i in range(10))
print(tuple_A)
# >>>><generator object <genexpr> at 0x000001695FA62350>
tuple_B = tuple(tuple_A)          #当元组被转化后，tuple_A已经变成了空元组
print(tuple_B, tuple(tuple_A))
# >>>>(54, 26, 81, 57, 65, 27, 70, 42, 85, 88) ()


#元组的拼接及修改
tupel1 = ('A', 'B', 'C')
tupel2 = ('X', 'Y', 'Z')
tupel_a = tupel1 + tupel2
print(tupel_a) 