#字典类型
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

#取值
print(d['Michael'])
print(d.get('Michael'))
print(d.get('Michael2','notExist'))


#set
s = set([1, 1, 2, 2, 3, 4,3])
print(s)

#set 添加删除元素
s.add(4)
s.remove(4)