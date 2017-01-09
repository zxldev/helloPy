# -*- coding: utf-8 -*-
import os

#
#打开并读取打印文件
try:
    f = open('doFile.py','r')
    print(f.read())
except:
    print('error')
finally:
    if f:
        f.close()

#with语法， 可以不写f.close
with open('doFile.py','r') as f:
    print(f.read())


#二进制文件
f = open('write.txt','a')
f.write('hello test\n')
f.close()

#系统类型
print(os.name)
#系统信息
print(os.uname())
#配置
print(os.environ)
print(os.environ.get('PATH'))
print(os.environ.get('unExistKey','defaultValue'))



# 查看当前目录的绝对路径:
currentPath = os.path.abspath('.')
print(currentPath)

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
newPath = os.path.join(currentPath, 'testdir')
print(newPath)

# 然后创建一个目录:
try:
    os.mkdir(newPath)
except FileExistsError as e:
    pass
finally:
    pass

#分割文件名和路径
print(os.path.split(newPath))
#分割路径和扩展名
print(os.path.splitext(newPath))
#列出文件夹下的文件
print(os.listdir('.'))

# 删掉一个目录:
os.rmdir(newPath)

