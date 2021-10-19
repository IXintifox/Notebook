import re

class Data:

    def __init__(self, p_num):

        self.n = p_num     #接受传递参数

    def judge(self):

        num = r'(13[4-9]\d{8}|18[4-9]\d{8})$'      #按照位数排列
        numd = self.n            #调用self
        num_c = re.match(num,numd)     #使用函数

        #结果判定
        if bool(num_c) == 1:
            print('号码符合条件')
        else :
            print('不符合条件')

numd1 = '13607986875'
numd2 = '13109798877'

#numd1调用
p_number = Data(numd1)      #传递参数给class
p_number.judge()           #调用class函数中的judge

#num2调用
p_number = Data(numd2)
p_number.judge()

