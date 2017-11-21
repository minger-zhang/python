#!/usr/bin/env python
#-*- coding: utf-8 -*-
from define_func import Student
from define_func import Student1
from define_func import Student2
from define_func import Student3
from define_func import Student4
from define_func import Screen
from types import MethodType

s = Student()
s.name ="xiaomi"
s.age = 23
s.ss = 99
print(s.name,s.age,s.ss)


s1 = Student1()
s1.name = "xiaoju"
s1.age = 21
#s1.ss = 99
print(s1.name,s1.age)#s1.ss)


def set_age(self,age):
    self.age = age
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)


s = Student2()
s.set_score(60)
s.get_score()

#s.set_score(10000)



s1 = Student()
s.score = 60
print(s.score)

s.score = 9999


s2 = Screen()
s2.width = 1024
s2.height = 768
print('resolution = ', s2.resolution)
if s2.resolution == 786432:
    print('test pass!')
else:
    print('test fail!')



