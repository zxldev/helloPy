#定义函数
def fib(n):
    if n == 1 :
        return 1
    else:
        return n+fib(n-1)

#空函数
def nofun():
    pass

#空块
def funEmptyBlock(n):
    if n == 0:
        pass
    return n

#返回多个值
def calcSquart(n):
    return n*4,n*n

#汉诺伊塔 = = ! 这个是什么鬼实现
def moveGhost(n, a, b, c):
    if n == 1 :
        print(a, "==>", c)
    elif n == 2:
        print(a, "==>",b)
        print(a, "==>", c)
        moveGhost(1,b,a,c)
    else:
        for i in range(0,n-2):
            print(a,"==>",c)
        print(a,"==>",b)
        for i in range(0, n - 2):
            print(c, "==>", b)
        print(a,"==>",c)
        moveGhost(n-1,b,a,c)

#汉诺伊第归实现
def move(n,a,b,c):
    if n == 1:
        print(a, "==>", c)
    else:
        move(n-1,a,c,b)
        print(a, "==>", c)
        move(n - 1, b, a, c)


def funFor():
    d = {'a': 1, 'b': 2, 'c': 3}
    for value in d:
        print(value,d[value])