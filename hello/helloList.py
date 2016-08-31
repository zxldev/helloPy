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
for list in L:
    for e in list:
        #不打印换行符方式
        print(e, '',end="")
    print ('\n')

ceshi = list(range(10))
print()