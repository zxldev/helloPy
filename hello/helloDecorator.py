'a test model'

__author__ = 'zxldev'


import functools
#传参数装饰器
def log(text):
    def callfun(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text ,func.__name__))
            return func(*args, **kw)
        return wrapper
    return  callfun



#前后返回值装饰器
def surround(func):
    @functools.wraps(func)
    def wapper(*args, **kw):
        print('begin %s():' %  func.__name__)
        ret = func(*args, **kw)
        print('end %s():' % func.__name__)
        return  ret
    return wapper

@surround
def now():
    print ('20160905')


f = now

f()