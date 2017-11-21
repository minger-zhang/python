#!/usr/bin/env python
#-*- coding: utf-8 -*-
from enum import Enum
from define_fun import Student
from define_fun import Gender
from define_fun import User

#Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
Month = Enum("Month",('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
for name,member in Month.__members__.items():
    print(name,'=>',member,member.value)

bart = Student('Bart',Gender.Male)
if bart.gender == Gender.Male:
    print('test pass')
else:
    print('test faile')

u = User(id=1234,name='Micheal',email='test@orm.org',password='my-pwd')
u.save()


