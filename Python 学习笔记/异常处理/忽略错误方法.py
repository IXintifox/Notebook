def division(a,b):
    return a/b

try:
    a,b = input('输入两个数').split(' ')
    print (division(int(a),int(b)))
except ZeroDivisionError:      #零除错误
    print('分母不能为零')

except TypeError :
    print('不能输入此类数据{}，类型错误'.format(a,b))

except ValueError :
    print('输入值错误：',a,b)