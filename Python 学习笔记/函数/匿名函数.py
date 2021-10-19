bookinfo = [('A',2),('B',4),
            ('C',1),('D',3)]
print('book\n',bookinfo,'\n')
bookinfo.sort(key=lambda x:x[1])    # 按指定规则进行排序  x代表元组
print('排序后的商品信息：\n',bookinfo)
