#!/usr/bin/env python
#-*- coding: utf-8 -*-
#############multiple inheritance#################
class Father(object):
    def func(self):
        print('Father hit son')

class LaoWang(object):
    def func(self):
        print('Wang hit son')
    def func1(self):
        print('talk to your mother I will back')

class StepFather(object):
    def func(self):
        print('StepFather hit son')
    def func1(self):
        print('I will hit your mother')


class Mysterious(Father,LaoWang,StepFather):
    pass


#################Custom class############
####__repr__:for develeper debug msg
####__str__: for customer show msg
class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__


#########################################################
class Fib(object):
    def __init__(self):
        self.a,self.b = 0, 1
    def __iter__(self):
        return self
    ###def next(self): for python2.7
    ###def __next(self): for python3.x
    def next(self):
        self.a, self.b = self.b,self.a+self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a
    def __getitem__(self,n):
    ###for like list can get any element
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b , a + b
            return a 
    ###for like list can get any element form n:m
        if isinstance(n,slice):
            start = n.start
            stop  = n.stop
            step  = n.step
            if start is None:
                start = 0
            if step is None:
               step = 1
            a,b = 1,1
            L = []
            if (stop == None) or (stop < 0) or (start < 0) or (step < 0):
	       stop = 0
               step = 0
               print('Not Suitable input')
               L = ''
            for x in range(stop):
                if x >= start:
                    L.append(a)
                for m in range(step):
                   a,b = b, a+b
            return L 
        
#################__getattr__###################
class Student1(object):
    def __init__(self):
        self.name = 'Micheal'
    def __getattr__(self,attr):
        if attr == 'score':
            return 99   
        if attr == 'age':
            return lambda:25
        raise AttributeError('\'Student1\' object has no attribute\'%s\'' % attr)  
     

##########test auto __getattr__#################
class Chain(object):
    def __init__(self,path=''):
        self._path = path
    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path, path))
    def users(self,value):
        return Chain('%s/%s' % (self._path, value))
    def __str__(self):
        return self._path
    __repr__ = __str__

#########__call__()######################
class Student2(object):
    def __init__(self,name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)




