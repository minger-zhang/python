#!/usr/bin/env python
#-*- coding: utf-8 -*-
from abstest import my_abs
from abstest import nop
from abstest import move
import math
from abstest import quadratic
from abstest import power
from abstest import person

#########test list add dict & set###########
######[2,3]is a list ,unhash,typeerror
L1 = (1,[2,3])
#s1 = set(L1)
#print(s1)

L2 = (1,2,3)
s2 = set([1,2,3])
print(s2)
s2.add(L2)
print(s2)
#s2.add(L1)
#print(s2)


d = {'one':12,'two':34,'three':56}
d[L2] = 78
print(d)
####L1 containt list,unhash typeerror
#d[L1] = 99
#print(d)




#####################test part two################
n1 = 255
n2 = 1000

print('n1 = %d = %s' % (n1,hex(n1)))
print('n2 = %d = %s' % (n2,hex(n2)))


##################test part three#################
##########define function

#def my_abs(x):
#    if x >= 0:
#       return x
#    else:
#       return -x

x = 100
y = -100
print('x =',my_abs(x))
print('y =',my_abs(y))
#my_abs('A')
nop()
x1,y1 = move(100,100,60,math.pi / 6)
print(x1,y1)

print(quadratic(2,3,1))
print(quadratic(1,3,-4))

print(power(5))
print(power(5,3))


person('Micheal',30)
person('Bob',35,city='Beijing')
person('Adam',45,gender='M',job='Engineer')
extra = {'city':'Beijing','job':'Engineer'}
person('Jack',28,**extra)




