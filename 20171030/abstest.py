#!/usr/bin/env python
#-*- coding: utf-8 -*-
import math

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
       return x
    else:
       return -x


def nop():
    pass

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny


def quadratic(a,b,c):
    x1 =(((-b)+ math.sqrt(b*b - 4*a*c))) / (2*a)
    x2 =(((-b)- math.sqrt(b*b - 4*a*c))) / (2*a)
    return x1,x2

def power(x,n=2):
    s = 1
    while n > 0:
       n = n - 1
       s = s * x
    return s


def add_end(L=None):
    if L is None:
       L = []
    L.append('END')
    return L

####*numbers is variable arguments
def calc(*numbers):
    sum = 0
    for n in numbers:
          sum = sum + n*n
    return sum


def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)


