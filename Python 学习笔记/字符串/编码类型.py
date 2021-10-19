#编码类型所占字符大小

string = 'Python的使用方法'
print(len(string.encode('gbk')))    #gbk编码格式输出
print(len(string.encode('UTF-8')))
    #编码类型输出
print(string.encode('GBK'))
print(string.encode('UTF-8'))   #同理，解码装置 print(st.decode(encoding = 'UTF-8'))
#格式化输入

    #%09d类型
temple = '编号:%09d\t 名称:%s\t  网址:http://www.%s.com'
ins = (7,'INTIFOX','INTIFOX')
print(temple%ins)

    #{:s}类型
temple1 = '编号:{:0>9s}\t 名称:{:s}\t  网址:http://www.{:s}.com'
print(temple1.format('XXXX','INTIFOX','INTIFOX'))

#字符串切割

    #[]切割

str1 = '人生苦短，我用Python'
print (str1[1:])
print (str1[:4])      #带左不带右
print (str1[1:4])

    #split切割

str2 = '人生苦短，我用>>>Py>>>th<<<on<<<'
print(str2.split('，'))
print(str2.split('>>>'))    #全分割
print(str2.split('>>>',1))    #仅仅分割一个

