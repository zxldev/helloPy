# -*- coding: utf-8 -*-
#有序集和
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

#集合长度
print(len(classmates))

#插入数据
classmates.insert(1, 'Jack')
print(classmates)

#数组示例
L = [['Apple', 'Google', 'Microsoft'],    ['Java', 'Python', 'Ruby', 'PHP'], ['Adam', 'Bart', 'Lisa']]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

print('\n==============\n')

#循化语句
for l in L:
    for e in l:
        #不打印换行符方式
        print(e, '',end="")
    print ('\n')


#切片
S = list(range(100))
print(S)
print(S[1:6])
print(S[:6])
print(S[-6])
print(S[-6:-1])
print(S[:])
#步长为2
print(S[1:6:2])
print(S[1::10])
#字符串的切片
print('你好，我是admin'[::2])
print((1,2,3,4,5)[::2])


