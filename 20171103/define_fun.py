#!/usr/bin/env python
#-*- coding:utf-8 -*-

def _private_1(name):
    return 'Hello,%s' % name

def _private_2(name):
    return 'Hi,%s'  %  name

def greeting(name):
   if len(name) > 3:
       return _private_1(name)
   else:
       return _private_2(name)


class Student(object):
    
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s' % (self.name,self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
#####################counld change name and score out of class###############################
 

class Student1(object):
    
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name,self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')



##############################################OOP subclass & base class super class
class Animal(object):
    def run(self):
        print('Animal is running......')


class Dog(Animal):
    
    def run(self):
        print('Dog is running...')
   
    def eat(self):
        print('Eating Meat...')


class Cat(Animal):
#    pass
    def run(self):
        print('Cat is running ...')




def run_twice(animal):
    animal.run()
    animal.run()


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

















