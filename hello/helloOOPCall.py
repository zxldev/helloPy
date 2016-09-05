from hello import helloOOP


stu = helloOOP.Student('zxl',90)
stu.print_score()




obj = [helloOOP.Cat(),helloOOP.Animal(),helloOOP.Dog()]

def run(obj):
    obj.run()

list(map(run,obj))