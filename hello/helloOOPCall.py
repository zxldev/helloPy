from hello import helloOOP


stu = helloOOP.Student('zxl',90)
stu.print_score()




obj = [helloOOP.Cat(),helloOOP.Animal(),helloOOP.Dog()]

def run(obj):
    obj.run()

list(map(run,obj))

#获取对象类型
print(type(obj))
dog = helloOOP.Dog()
print(type(dog))

#判断是否为某种类型
print(isinstance(dog,helloOOP.Dog))
print(isinstance(obj,helloOOP.Dog))

#列出所有属性
print(dir(dog))
print(dir("a test string"))