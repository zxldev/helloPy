
#循环迭代器，带条件[和生成器的区别在于 “[]” 变为了 “()”]
g=( (a,b,c) for a in range(1,100) for b in range(a,100) for c in range(b,100) if (a*a + b*b == c*c))
for n in g:
    print(n)

#函数迭代器 【将print替换为yield】
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        #注意此处
        yield(b)
        a,b = b ,a+b
        n = n +1
    return 'done'

print(list(fib(10)))

#作业
def triangles():
    l = [1]
    while 1:
        yield (l)
        l1 = [0] + l
        l = [l1[i]+l1[i+1] for i in range(len(l))]+[1]



n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 20:
        break