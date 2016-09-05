class Animal(object):
    def eat(self):
        print('animal eating')

class Flyable(object):
    def fly(self):
        print('flying')

class Runable(object):
    def run(self):
        print('running')
    def eat(self):
        print('run with eating')

class Dog(Animal,Runable):
    pass

#注意和Dog类的顺与，前面Runable类的run会覆盖后面Animal类的run方法
class RunDog(Runable,Animal):
    pass

class FlyingDog(Dog,Flyable):
    pass

dog = Dog()
rundog = RunDog()
dog.eat()
rundog.eat()
dog.run()

flydog = FlyingDog()
flydog.fly()