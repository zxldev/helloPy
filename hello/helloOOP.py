class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s : %s'%(self.name,self.score))

class Animal(object):
    def __init__(self):
        pass

    def run(self):
        print('Animal is running.')

class Dog(Animal):
    def run(self):
        print('Dog is running.')

class Cat(Animal):
    def run(self):
        print('Cat is running.')