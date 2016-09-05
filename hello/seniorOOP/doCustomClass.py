#双下划线开头的方法有特殊用途
#Python的class中有许多特殊用途的函数，可以帮助我们定制类。

#__str__
class Student(object):
    def __init__(self,name):
        self._name = name
        self._class = ['math', 'music','test','test2','test3']
        self._index = 0

    #打印字符时返回的字符串
    def __str__(self):
        return 'student\'s name is %s'%(self._name)

    __repr__ = __str__

    #迭代对象， 和__next__一起使用
    def __iter__(self):
        return self

    def __next__(self):
        if self._index > len(self._class)-1:  # 退出循环的条件
            raise StopIteration()
        ret = self._class[self._index]
        self._index = self._index + 1
        return  ret

    #list操作，取元素，切片等操作
    def __getitem__(self,n):
        return self._class[n]

    #没有元素,就去字典中取值
    def __getattr__(self,name):
        try:
            return object.__getattribute__(name)
        except Exception:
          return None

    #是否可执行
    def __call__(self, *args, **kwargs):
        print(self.__str__())



s = Student('zxldev')
print(s)

for c in s:
    print(c)

print(s[:3])

s.bbb = '2'
print(s.bbb)

#调用对象s
s()