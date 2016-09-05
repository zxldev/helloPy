# -*- coding: utf-8 -*-

import os
#生成列表
print([x*x for x in range(1,50)])
#带条件生成
print([x*x for x in range(1,50) if x % 5 == 0])
#循环生成
print ([(m,n) for m in 'ABC' for n in range(1,6)])
#循环生成，带条件
print([ (a,b,c) for a in range(1,100) for b in range(a,100) for c in range(b,100) if (a*a + b*b == c*c)])

#打印当前目录文件
print ([file for file in os.listdir('.') if file != '__init__.py'])

#调用函数
L = ['Hello', 'World', 'IBM', 'Apple']
print ([l.lower() for l in L])

#作业
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [l.lower() for l in L1 if isinstance(l,str)]
print (L2)