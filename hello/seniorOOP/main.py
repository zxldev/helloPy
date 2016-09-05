from hello.seniorOOP import doSlots
from hello.seniorOOP import doProperty

#没有使用slots可以添加对象属性
stu1 = doSlots.Student()
stu1.name = 'zxldev'
stu1.notexist = "test"
print(stu1.name)
print(stu1.notexist)


    

#使用slots,不可以可以添加对象属性
stu1 = doSlots.StudetnWithSlots()
stu1.name = 'zxldev'
print(stu1.name)
#以下代码将报错
#stu1.notexist = "test"
#print(stu1.notexist)

#测试@property
s = doProperty.Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution