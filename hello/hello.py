#hello world
print("hello world!")
#字符串链接
print('The quick brown fox', 'jumps over', 'the lazy dog')
#算术表达
print(100 + 200)
#算术表达2
print('100 + 200 =', 100 + 200)


#缩进风格和分支判断
# print absolute value of an integer:
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

#转义字符
print('I\'m ok.')
print('I\'m \"OK\"!')
#如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义
print('\\\t\\')
print(r'\\\t\\')
#如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容
print('''line1
line2
line3''')

#比较运算符
age = 17
if age >= 18:
    print('adult')
else:
    print('teenager')

#//，称为地板除，两个整数的除法仍然是整数
print(10//3)

#python支持中文输入
print('python支持中文输入，包含中文的str')

print('\u4e2d\u6587')

#字符串格式化 在Python中，采用的格式化方式和C语言是一致的，用%实现
print( 'Hi, %s, you have $%d.' % ('Michael', 1000000))

