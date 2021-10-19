List1 = ['physics', 'chemistry', 1997, 2000, ['x', 'y', 'z']]
List2 = ['physics', 'chemistry', 1997, 2000]
List_num = [97, 36, 59, 16, 19, 96, 6, 54, 99, 70]
List_char = ['cat', 'Tom', 'pat', 'Angel']
#列表遍历
for i in List1:
    print(i)

#列表元素查询
print('list:' + List1[4][1])

#列表增添/删除元素
List1.append(407)
print('append 407:' + str(List1))
List1[4].append('A')
print('append A:' + str(List1))
List1.remove(1997)
print('remove 1997:' + str(List1))
del List1[-2]          #按照index删除元素
print('del:' + str(List1))

#列表索引定位
print('index:' + str(List1.index(407)))   #仅为首次出现的下标

#列表索引
for item, j in enumerate(List2):
    print(item, j)

#列表扩增,是否修改原列表
List3 = List1+List2
print('List3:'+str(List3))
List1.extend(List2)
print('List4:'+str(List1))

#列表元素计数
print('407的数量为：'+str(List1.count(407)))

#列表数相加
print('Add = ' + str(sum(List_num)))

#列表的排序/数字+字符串
    #已经改变原本字符串
List_num.sort(reverse=False)     #False为升序序列，True为降序
print("列表升序:"+str(List_num))

List_char.sort()
print('按字母排序，先大后小'+str(List_char))
List_char.sort(key=str.lower)
print('先小后大'+str(List_char))

    #不改变原有字符串
List_origin = sorted(List_num,reverse=True)
print('排序后'+str(List_origin))
print('原列表'+str(List_num))

