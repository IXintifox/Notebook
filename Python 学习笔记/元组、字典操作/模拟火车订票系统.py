Train = {'T40':'长春-北京', 'T298':'长春-北京', 'Z158':'长春-北京', 'Z62':'长春-北京'}
Departure_time = {'T40':'00:12', 'T298':'00:06', 'Z158':'12:48', 'Z62':'21:58'}
Arrive_time = {'T40':'12:20', 'T298':'10:50', 'Z158':'21:06', 'Z62':'06:08'}
Long = {'T40':'12:08', 'T298':'10:44', 'Z158':'08:18', 'Z62':'8:20'}


Train_number = input('请输入要购买的车次\n')
Person1, Person2 = input('请输入乘车人（用逗号分隔）').split(',')


print('您已购入{}次列车 {} {}开，请{}，{}尽快换取纸质车票。【铁路客服】'.format(Train_number,Train[Train_number],Departure_time[Train_number], Person1, Person2))