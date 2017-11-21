#!/usr/bin/env python
#-*- coding: utf-8 -*-
from define_fun import Mysterious
from define_fun import Student
from define_fun import Student1
from define_fun import Student2
from define_fun import Fib
from define_fun import Chain


s = Mysterious()
s.func()
s.func1()


s1 = Student('Micheal')
print(s1)
 


for n in Fib():
    print(n)

print(Fib()[5])
print(Fib()[5:10])

f = Fib()
print(f[:11:2])

###test new part
print(Fib()[:19])
print(Fib()[:19:2])
print(Fib()[2:])
print(Fib()[-2:2])




s1 = Student1()
print(s1.name)
#s1.name
###'Student1' object has no attribute 'score'
#print(s1.score) 
####test modify Student1 add __getattr__ function
print(s1.score)
#####test modify Student1 add __getattr__ funtion return age()
print(s1.age())
#####test Student1 object has no attribute 'sex'
#print(s1.sex)


#################test Auto __getattr__##########
print(Chain().status.user.timeline.list)
###would try to do
print(Chain().users('minger-zhang').repos)

#################__call__()##################
s2 = Student2('Micheal')
s2()
####callable
print(callable(Student2('Micheal')))
print(callable([1,2,3]))









