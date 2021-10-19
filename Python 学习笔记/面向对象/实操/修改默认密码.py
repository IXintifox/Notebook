class Person:
    def __init__(self, card_number = 8479847203443, password = 123456):
        self.__card_number = card_number
        self.__password = password

    @property
    def account(self):
        return 'Card number:' + str(self.__card_number)

    @property
    def pass_num(self):
        return 'Password:' + str(self.__password)


    @pass_num.setter
    def pass_num(self,value):
        if value != self.__password:
            self.__password = value
            print('密码修改成功，新密码为：{}'.format(self.__password))
        else:
            print('请输入不同密码')

person = Person()

print(person.account, person.pass_num)

print('请输入修改的密码：')
person.pass_num = int(input(''))
print(person.account, person.pass_num)





