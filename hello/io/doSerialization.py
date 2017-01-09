# -*- coding: utf-8 -*-
import json

d = dict(
    name='Bob',
    age=20,
    score=88
)

#json序列化
jsonstr = json.dumps(d)

print(jsonstr)
print(type(jsonstr))

#json反序列化
dEntity = json.loads(jsonstr)

print(dEntity)
print(type(dEntity))


