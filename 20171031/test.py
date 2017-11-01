#!/usr/bin/env python
#-*- coding: utf-8 -*-
from define_fun import move
from collections import Iterable
from define_fun import fib
from define_fun import triangles
import os


move(3,'A','B','C')


##########iteration######################
#####example 1
d = {'a':1,'b':2,'c':3,'d':4}
for key in d:
     print(key)

#####example 2
for value in d.values():
     print(value)

#####example 3
for k,v in d.items():
     print(k,v)

#####test argument can be iterable or not
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))


################list genrate ##############
print(list(range(1,11)))
##############
L = []
for x in range(1,11):
     L.append(x*x)
print(L)

######instead of
L = [x*x for x in range(1,11)]

print(L)

L = [x*x for x in range(1,11) if x %2 == 0]
print(L) 

L = [m+n for m in 'ABC' for n in 'XYZ']
print(L)

##########print dir
L = [d for d in os.listdir('.')]
print(L)


#########test two parament 
d = {'x':'A','y':'B','Z':'C'}
for k,v in d.items():
      print(k,'=',v)

##########equl 
d = {'x':'A','y':'B','Z':'C'}
L = [k + '=' + v for k,v in d.items()]
print(L)

#############to be lower
L = ['Hello', 'Worle', 'IBM', 'Apple']
L1 = [s.lower() for s in L]
print(L1)


##############################################################
L = ['Hello', 'World', 18, 'Apple',None]
L1 = [s.lower() if isinstance(s,str) else s for s in L]
L2 = []
[L2.append(i.lower()) for i in L if isinstance(i,str)]
print(L1)
print(L2)


######################genration#########################################
f = fib(6)
while True:
     try:
         x = next(f)
         print('f:',x)
     except StopIteration as e:
         print('Generator return value:',e.value)
         break


########################triangles#########################################
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 15:
       break





