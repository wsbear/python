while True:
    a=int(input('请输入一个数'))

    if a==1:
        print('是质数')
    for i in range(2,a):
        if a%i==0:
            print('不是质数')
            break
        elif i==a-1:
            print('是质数')
