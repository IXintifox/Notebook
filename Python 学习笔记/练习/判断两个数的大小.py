
while True:
    try:
        a, b = input('输入两个数').split(' ')
        print(a, b)
        if a == b:
            print('{}={}'.format(a, b))
        elif a > b:
            print('{}>{}'.format(a, b))
        elif a < b:
            print('{}<{}'.format(a, b))
    except EOFError:
        break



