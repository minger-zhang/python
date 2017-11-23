#!/usr/bin/env python
#-*- coding: utf-8 -*-
from functools import reduce
import pdb
import platform


class FooError(ValueError):
    pass


def str2num(s):
    try:
       pdb.set_trace()
       return int(s)
    except ValueError as e:
        print('invalid value:%s' % s)
    finally:
       return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num,ss)
    return reduce(lambda acc, x : acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 = ' ,r)
    r = calc('99 + 88 + 7.6 ')
    print('99 + 88 + 7.6 = ' , r)



class Dict(dict):

    def __init__(self,**kw):
        if platform.python_version() == '2.7.3':
            super(Dict,self).__init__(**kw)
        else:
            super().__init__(**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self,key,value):
        self[key] = value


class Student(object):
  
    def __init__(self,name,score):
        self.name  = name
        self.score = score
    def get_grade(self):
        if 80 < self.score >= 60:
            return 'B'
        if self.score >= 80:
            return 'A'
        return 'C'













