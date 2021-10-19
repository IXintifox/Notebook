import re
url = 'https://zhidao.baidu.com/question/501423560809334564.html?qbl=relate_question_0&word=findall%BA%AF%CA%FD%B7%B5%BB%D8%CA%B2%C3%B4'
ct = r'[?|&]'   #切割需要正则化标签[ ]

ctd = re.split(ct, url)    #可加切割次数，标志位（maxsplit,flags）
print(ctd)