#!/usr/bin/env python
#-*- coding: utf-8 -*-
from define_fun import lazy_sum
from define_fun import count
from define_fun import count1
from define_fun import log
from define_fun import now
from define_fun import test_now
from define_fun import test_now1
from define_fun import test_now3
from define_fun import test_now4
from define_fun import test_now5


################test lazy_sum
f = lazy_sum(1,3,5,7,9)
print(f)
print(f())


f1 = lazy_sum(1,3,5,7,9)
print(f1)
print(f1())

print(f == f1)


f1,f2,f3 = count()
print(f1(),f2(),f3())


f1,f2,f3 = count1()
print(f1(),f2(),f3())

################################decorator
#now()
#now =  log('execute')(now)


#print(now())
#print(now.__name__)

#print(test_now())

#print(test_now1())

print(test_now3())

print(test_now4())
print(test_now5())



